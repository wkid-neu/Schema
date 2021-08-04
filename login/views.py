import hashlib
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from login import models
from neomodel import db
from login.forms import UserForm, RegisterForm
import global_data
from createobject.to_class import TransClass
from pandas._libs import json


# Create your views here.


def index(request):
    return render(request, "login/index.html")


def kg_index(request):
    if request.session.get('is_login', None):
        return render(request, "login/choose.html")

    else:
        return render(request, "login/nologin.html")


def display(request):
    user_id = request.session.get("user_id")
    if request.session.get('extract', None) is None:
        print("用户的图谱取出来了。")
        set_entities_data(user_id)
        request.session['extract'] = True
    return render(request, "KGPage/display.html")


def search(request):
    return render(request, "createobject/search.html")


def get_md5(password, salt='breeze'):
    md5 = hashlib.md5()
    md5.update((password + salt).encode())
    return md5.hexdigest()


def set_entities_data(user_id):  # 《======================-----------------------待修改的地方
    created_entities = global_data.get_created_entities()
    created_classes = global_data.get_created_classes()
    transfer = TransClass(user_id)
    transfer.transfer()
    entity_list = {}
    for entity in transfer.entity_class_json:
        for obj in transfer.entity_class_json[entity]:
            entity_list[obj['node_id']] = [entity, transfer.result[obj["node_id"]]["fill_data"], 1]  # 1代表已经进入图谱
    created_entities[user_id] = entity_list
    class_list = {}
    for obj in transfer.result:
        class_list[obj] = transfer.result[obj]["class"]
    created_classes[user_id] = class_list
    print(created_classes)
    print(created_entities)
    global_data.set_created_enetities(created_entities)
    global_data.set_created_classes(created_classes)
    entities_json = json.dumps({'nodes': transfer.nodes, 'links': transfer.links})
    json_path = "D:\pycharm\Projects\Schema\static\KGJson\{}_nodes_json.json".format(user_id)
    try:
        with open(json_path, 'w', encoding='utf-8') as f:
            f.write(entities_json)
            f.close()
        print("图谱转换JSON成功！")
    except Exception as e:
        print("图谱转换JSON失败！")


def login(request):
    if request.session.get('is_login', None):
        return redirect('/index')
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.UserinfoTab.objects.get(name=username)
                if user.password == get_md5(password + username):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = "密码不正确!"
            except Exception as e:
                message = "用户不存在!"
        return render(request, 'login/login.html', locals())
    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.UserinfoTab.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.UserinfoTab.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.UserinfoTab.objects.create()
                new_user.name = username
                new_user.password = get_md5(password1 + username)
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/index/")
    request.session.flush()
    return redirect("/index/")
