import threading
from datetime import datetime

from django.db import models
from django.shortcuts import render
import json
import os
from login import models
import Schema.settings as settings
from django.shortcuts import HttpResponse
from PreprocessData.all_class_files.all_class import *
from objTonode.to_class import TransClass
from objTonode.to_node import TransNode
from objTonode.process_node import delete_kg


# Create your views here.


def map_index(request, type):
    request.session["app_name"] = "MapSchema"
    if request.session.get('is_login', None):
        if type == "address":
            return render(request, 'display/address.html')
        elif type == "enter":
            return render(request, 'display/enter.html')
    else:
        return render(request, "login/nologin.html")


def set_allmarkers_data(user_id):
    transfer = TransClass(user_id, "MapSchema")
    transfer.transfer(extract_all=True)
    entity_list = {}
    for entity in transfer.entity_class_json:
        for obj in transfer.entity_class_json[entity]:
            entity_list[obj['node_id']] = [entity, transfer.result[obj["node_id"]]["fill_data"],
                                           transfer.result[obj["node_id"]]["monitor_id"]]
    global_data.set_mappoints(entity_list)
    global_data.set_kg_ids(transfer.kg_ids, "MapSchema")
    print(global_data.get_kg_ids())
    entities_json = json.dumps({'nodes': transfer.nodes, 'links': transfer.links}, ensure_ascii=False)
    json_path = os.path.join(settings.STATICFILES_DIRS[0], "KGJson\MapSchema_nodes_json.json")
    try:
        with open(json_path, 'w', encoding='utf-8') as f:
            f.write(entities_json)
            f.close()
        print("图谱转换JSON成功！")
    except Exception as e:
        print("图谱转换JSON失败！")
        print(e)


def process_date(val_list):
    result = []
    for obj in val_list:
        if type(obj).__name__ == "str":
            result.append(obj)
        elif type(obj).__name__ == "date":
            result.insert(0,obj.strftime("%Y"))
    return result


def get_all_points(request):
    if global_data.global_var.MAP_FLAG == False:
        global_data.set_MAP_FLAG(True)
        user_id = request.session.get("user_id")
        set_allmarkers_data(user_id)
    markpoint_data = global_data.get_mappoints()
    address_longitude = []
    address_latitude = []
    address_data = []
    for id in markpoint_data:
        if markpoint_data[id][0] == "CreativeWork":
            property_list = markpoint_data[id][1]
            temp_data = {'building_name': property_list['name'], 'title': property_list['headline'],
                         "cre_date": process_date(property_list['dateCreated']),
                         "img_description": property_list['description'],
                         "encode_type": property_list['encodingFormat'],
                         "type": property_list['keywords'], "file_url": property_list['citation'],
                         "creator": property_list["creator"][0].name,
                         "location": property_list["mentions"][0].address,
                         "building_information": property_list["mentions"][0].description,
                         "announcer": property_list["publisher"][0].name,
                         "CopyrightOwner": property_list["copyrightHolder"][0].name,
                         "img": property_list["mentions"][0].image,
                         "node_id": id, "monitor_id": markpoint_data[id][2]}
            address_longitude.append(property_list["mentions"][0].geo[0].longitude)
            address_latitude.append(property_list["mentions"][0].geo[0].latitude)
            address_data.append(temp_data)
    return HttpResponse(json.dumps({'address_longitude': address_longitude,
                                    'address_latitude': address_latitude,
                                    'address_data': address_data}))


def create_obj(class_name, property_list):
    module_meta = __import__("PreprocessData.all_class_files.all_class", globals(), locals(), [class_name])
    class_meta = getattr(module_meta, class_name)
    obj = class_meta(**property_list)
    return obj


def trans_date(cre_date):
    lens = len(cre_date.split("-"))
    if lens == 1:
        return datetime.strptime(cre_date, "%Y").date()
    if lens == 2:
        return datetime.strptime(cre_date, "%Y-%m").date()
    if lens == 3:
        return datetime.strptime(cre_date, "%Y-%m-%d").date()


def update(request):
    return render(request, "display/result.html")


def process_form(request):
    app_name = request.session.get("app_name")
    user_id = request.session['user_id']
    user_name = request.session['user_name']
    if request.method == "POST":
        file_obj = request.FILES.get("up_file")
        user_directory = os.path.join(settings.MEDIA_ROOT, "{}_files\\".format(user_name))
        file_path = os.path.join(user_directory, file_obj.name)
        try:
            f1 = open(file_path, "wb")
            for i in file_obj.chunks():
                f1.write(i)
            f1.close()
        except Exception as e:
            print(e)
            print("文件读写失败！")
        relative_path = "..\\static\\upload_media\\{}_files\\{}".format(user_name, file_obj.name)
        lng = request.POST['lng']
        lat = request.POST['lat']
        building_name = request.POST['building_name']
        title = request.POST['title']
        creator_name = request.POST['creator']
        cre_date = request.POST['cre_date']
        date_str = request.POST['cre_date_str']
        location = request.POST['location']
        img_description = request.POST['img_description']
        encode_type = request.POST['encode_type']
        building_information = request.POST['building_information']
        announcer_name = request.POST['announcer']
        CopyrightOwner_name = request.POST['CopyrightOwner']
        file_url = request.POST['file_url']
        type_data = request.POST['type'].split(" ")
        creator = "Person"
        creator_property = {'name': [creator_name]}
        creator_obj = create_obj(creator, creator_property)
        CopyrightOwner = "Person"
        CopyrightOwner_property = {'name': [CopyrightOwner_name]}
        CopyrightOwner_obj = create_obj(CopyrightOwner, CopyrightOwner_property)
        announcer = "Organization"
        announcer_property = {'name': [announcer_name]}
        announcer_obj = create_obj(announcer, announcer_property)
        GeoCoordinates = "GeoCoordinates"
        GeoCoordinates_property = {'name': ["GeoCoordinates"], "longitude": [lng], "latitude": [lat]}
        GeoCoordinates_obj = create_obj(GeoCoordinates, GeoCoordinates_property)
        building = "LandmarksOrHistoricalBuildings"
        building_property = {'name': [building_name], "address": [location], "description": [building_information],
                             "geo": [GeoCoordinates_obj],
                             "image": [relative_path]}
        building_obj = create_obj(building, building_property)
        Photograph = "Photograph"
        date_val = []
        if cre_date != "null":
            date_val.append(trans_date(cre_date))
        if len(date_str) != 0:
            date_val.append(date_str)
        Photograph_property = {'name': [building_name + "照片"], "headline": [title], "description": [img_description],
                               "keywords": type_data, "creator": [creator_obj], "publisher": [announcer_obj],
                               "mentions": [building_obj], "copyrightHolder": [CopyrightOwner_obj],
                               "encodingFormat": [encode_type], "citation": [file_url],
                               "dateCreated": date_val}

        print(Photograph_property)
        Photograph_obj = create_obj(Photograph, Photograph_property)
        trans_node = TransNode(user_id, "MapSchema")
        trans_node.to_node(Photograph_obj)
        set_allmarkers_data(user_id)

    return render(request, "display/result.html")


def delete_process(user_id, node_id):
    user_kg_ids = global_data.get_kg_ids()
    MapSchema_kg_ids = user_kg_ids["MapSchema"]
    delete_kg(MapSchema_kg_ids[int(node_id)])
    set_allmarkers_data(user_id)


def delete_point(request):
    user_id = request.session.get("user_id")
    if request.method == "POST":
        node_id = request.POST.get("node_id")
    thread1 = threading.Thread(target=delete_process, args=(user_id, node_id,))
    thread1.start()
    return render(request, "display/result.html")


def edit_users(request):
    obj = models.UserinfoTab.objects.all().values()
    return render(request, "display/editusers.html", {'result': obj})


def edit_process(request):
    if request.method == "POST":
        update_data = json.loads(request.POST.get("update"))
        try:
            for obj in update_data:
                models.UserinfoTab.objects.filter(name=obj[0]).update(role=obj[1])
        except Exception as e:
            print(e, "更改失败!")
            return HttpResponse(json.dumps({'status': 0}))
        return HttpResponse(json.dumps({'status': 1}))
