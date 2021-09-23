import hashlib
import os
from datetime import time, datetime

from django.contrib.sessions.models import Session
from django.db.models import Q
from django.utils import timezone

import Schema.settings as settings

from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from login import models
from neomodel import db
from login.forms import UserForm, RegisterForm
from pandas._libs import json


# Create your views here.


def index(request):
    if request.session.get("is_login", None):
        return render(request, "display/address.html")
    return render(request, "login/index.html")


def display(request):
    return render(request, "KGPage/display.html")


def search(request):
    return render(request, "createobject/search.html")


def get_md5(password, salt='breeze'):
    md5 = hashlib.md5()
    md5.update((password + salt).encode())
    return md5.hexdigest()


def login(request):
    if request.session.get('is_login', None):
        return redirect('/index')
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            ip = request.META['REMOTE_ADDR']
            try:
                user = models.UserinfoTab.objects.get(name=username)
                if user.password == get_md5(password + username):
                    pduser = models.UserinfoTab.objects.filter(name=username).values()[0]["session"]
                    if pduser is None:
                        request.session['is_login'] = True
                        request.session['user_id'] = user.id
                        request.session['user_name'] = user.name
                        request.session['role'] = user.role
                        request.session["app_name"] = "MapSchema"
                        if not request.session.session_key:
                            request.session.save()
                        session_id = request.session.session_key
                        print(session_id,"sss")
                        ip = request.META['REMOTE_ADDR']
                        ####登录后，会生成session_key,将session_key写入到用户表的session里面
                        models.UserinfoTab.objects.filter(name=username).update(session=session_id, login_ip = ip)
                    else:
                        request.session.delete(pduser)
                        request.session['is_login'] = True
                        request.session['user_id'] = user.id
                        request.session['user_name'] = user.name
                        request.session['role'] = user.role
                        request.session["app_name"] = "MapSchema"
                        if not request.session.session_key:
                            request.session.save()
                        session_id = request.session.session_key
                        models.UserinfoTab.objects.filter(name=username).update(session=session_id)
                        # 获取登录IP
                        ip = request.META['REMOTE_ADDR']
                        models.UserinfoTab.objects.filter(name=username).update(login_ip=ip)
                        time_now = datetime.now().strftime("%Y-%m-%d %X")
                    models.LogininfoTab.objects.create(name=username, login_ip=ip, login_time=time_now, status="登录成功")
                    return redirect("/index/")
                else:
                    time_now = datetime.now().strftime("%Y-%m-%d %X")
                    models.Logininfo.objects.create(user=username, login_ip=ip, login_time=time_now, status="密码错误")
                    message = "密码不正确!"
            except Exception as e:
                message = "用户不存在!"
                print(e)
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
                new_user.role = "B"
                new_user.save()
                user_directory = os.path.join(settings.MEDIA_ROOT, "{}_files\\".format(username))
                print(user_directory)
                if not os.path.exists(user_directory):
                    os.makedirs(user_directory)
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/index/")
    request.session.flush()
    return redirect("/index/")
