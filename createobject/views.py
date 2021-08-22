import os
from datetime import datetime

from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import HttpResponse
from pandas._libs import json

from Schema import settings
from objTonode.to_class import TransClass
from createobject.models import EntityTab
from createobject.models import PropertyTab
from django.http import JsonResponse
from objTonode.to_node import TransNode
import global_data

imp_module = 'PreprocessData.all_class_files.{}'

range_table = global_data.get_table()
range_table_zh = global_data.get_table_zh()


def check(request):
    pass


def kg_index(request):
    request.session["app_name"] = "CreKg"
    user_id = request.session["user_id"]
    if request.session.get('is_login', None):
        created_entities = global_data.get_created_entities()
        if created_entities.get(user_id) is None:
            set_entities_data(user_id)
        return render(request, "createobject/choose.html")

    else:
        return render(request, "login/nologin.html")


def search(request):
    dest = request.GET['dest']
    result = []
    if dest != "":
        resultset = EntityTab.objects.filter(Q(name_zh__icontains=dest) | Q(entity_name__icontains=dest)).values(
            "entity_name", "name_zh")
        if resultset:
            for obj in resultset:
                result.append([obj['entity_name'], obj['name_zh']])
    print(result)
    return JsonResponse({'result': result})


def query_entity(entityname):
    entity_all_properties = EntityTab.objects.filter(entity_name=entityname).values("name_zh", "description",
                                                                                    "all_properties")
    all_properties_info = PropertyTab.objects.all().values()
    entity_data = {}
    entity_data['name'] = entityname
    entity_data['name_zh'] = entity_all_properties[0]['name_zh']
    entity_data['description'] = entity_all_properties[0]['description']
    entity_properties_set = entity_all_properties[0]['all_properties'].split(",")  # 要变成列表的，否则下面判断in的时候都会存在
    entity_properties_info = {}
    for obj in all_properties_info:
        if obj['property_name'] in entity_properties_set:
            entity_properties_info[obj['property_name']] = {'name_zh': obj['name_zh'],
                                                            'description': obj['description'],
                                                            'range_str': range_table[obj['property_name']],
                                                            'range_str_zh': range_table_zh[obj['property_name']]}
    entity_data['properties_info'] = entity_properties_info
    return entity_data


def creating(request, entityname):
    entity_data = query_entity(entityname)
    return render(request, "createobject/create.html", entity_data)


def process(request):
    user_id = request.session['user_id']
    created_classes = global_data.get_created_classes()
    created_entities = global_data.get_created_entities()
    if request.method == "POST":
        entity = request.POST.get('entity')
        storage_id = request.POST.get('id')
        property_data = json.loads(request.POST.get('property_data'))
        status = 1
        property_value = {}
        fill_data = {}
        for obj in property_data:  # 判断如果取值是类的话，从created_classes中取出对应的类赋给他
            value_list = []
            for value in property_data[obj]['value']:
                if value[0] == "obj":
                    fill_obj = value[1]
                    if fill_obj[0][0].isdigit() is False:
                        value_list.append(created_classes[user_id][fill_obj[0]])
                    else:
                        value_list.append(created_classes[user_id][int(fill_obj[0])])
                else:
                    if value[0] == 'date':
                        value_list.append(datetime.strptime(value[1], "%Y-%m-%d").date())
                    else:
                        value_list.append(value[1])
            property_value[property_data[obj]['eng_name']] = value_list
        try:
            module_meta = __import__("PreprocessData.all_class_files.all_class", globals(), locals(), [entity])
            class_meta = getattr(module_meta, entity)
            fill_data = property_value
            print(property_value)
            entity_obj = class_meta(**property_value)
            if not hasattr(entity_obj, 'node_id'):
                setattr(entity_obj, 'node_id', entity + str(storage_id))
        except Exception as e:
            print("创建失败！", e)
        created_classes[user_id][entity + str(storage_id)] = entity_obj
        created_entities[user_id][entity + str(storage_id)] = [entity, fill_data, 0]
        print("----", entity + str(storage_id))
        global_data.set_created_classes(created_classes)
        global_data.set_created_enetities(created_entities)
        print(created_classes)
        print(created_entities)
        return HttpResponse(json.dumps({
            "status": status,
        }))


def obtaining(request):
    created_entities = global_data.get_created_entities()

    user_id = request.session['user_id']
    return_json = []
    for obj in created_entities.get(user_id):
        return_json.append(
            {'id': obj, 'entity': created_entities[user_id][obj][0], 'name': created_entities[user_id][obj][1]['name'],
             'in_graph': created_entities[user_id][obj][2]})
    return HttpResponse(json.dumps(return_json))


def get_the_entity(request, entity_id):
    if entity_id[0].isdigit():
        entity_id = int(entity_id)
    created_entities = global_data.get_created_entities()
    properties_name_invert = global_data.get_properties_name_invert()
    user_id = request.session['user_id']
    return_json = {}
    print(created_entities)
    print(created_entities[user_id])
    fill_data = created_entities[user_id][entity_id][1]
    for obj in fill_data:
        return_json[properties_name_invert[obj]] = []
        for unit in fill_data[obj]:
            if type(unit).__name__ not in global_data.get_pre_data():
                return_json[properties_name_invert[obj]].append([unit.name[0], unit.node_id])
            else:
                return_json[properties_name_invert[obj]].append(unit)
    return render(request, "createobject/get_entity.html", {"result": return_json})


def set_entities_data(user_id):  # 《======================-----------------------待修改的地方
    created_entities = global_data.get_created_entities()
    created_classes = global_data.get_created_classes()
    user_kg_ids = global_data.get_kg_ids()
    CreKg_kg_ids = user_kg_ids["CreKg"]
    transfer = TransClass(user_id, "CreKg")
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
    CreKg_kg_ids[user_id] = transfer.kg_ids
    print(transfer.kg_ids)
    global_data.set_created_enetities(created_entities)
    global_data.set_created_classes(created_classes)
    global_data.set_kg_ids(CreKg_kg_ids, "CreKg")
    print(global_data.get_kg_ids())
    entities_json = json.dumps({'nodes': transfer.nodes, 'links': transfer.links}, ensure_ascii=False)
    json_path = os.path.join(settings.STATICFILES_DIRS[0], "KGJson\CreKg_{}_nodes_json.json").format(user_id)
    try:
        with open(json_path, 'w', encoding='utf-8') as f:
            f.write(entities_json)
            f.close()
        print("图谱转换JSON成功！")
    except Exception as e:
        print("图谱转换JSON失败！")
        print(e)


def generating(request):
    created_classes = global_data.get_created_classes()
    user_id = request.session['user_id']
    user_classes = created_classes[user_id]
    trans_node = TransNode(user_id, "CreKg")
    try:
        for obj in user_classes:
            if type(obj).__name__ == "int":
                continue
            trans_node.to_node(user_classes[obj])
    except Exception as e:
        print('生成图谱失败！', e)
    set_entities_data(user_id)
    return HttpResponse(json.dumps({}))
