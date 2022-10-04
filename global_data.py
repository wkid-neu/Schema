from django.db.models import Max
from py2neo import Graph
from PreprocessData.database_op import datasql


class global_var:
    graph = Graph("bolt://localhost:7687", username="neo4j", password='123123')
    pre_data = {"NoneType": "空值", "str": "自定义字符串", "Text": "自定义字符串", "Integer": "整数", "Bool": "布尔（真假）", "Date": "日期",
                "Float": "非整数"}
    msql = datasql()
    MAP_FLAG = False
    properties_data = msql.query("property_tab")
    user_kg_ids = {"CreKg": {}, "MapSchema": {}}
    properties_name_contrast = {}
    properties_name_invert = dict(zip([obj[0] for obj in properties_data], [obj[1] for obj in properties_data]))
    range_result = msql.query("range_tab")
    range_table = dict(zip([obj[0] for obj in range_result], [obj[1].split(',') for obj in range_result]))
    entity_result = msql.query("entity_tab")
    for obj in entity_result:
        properties_name_contrast[obj[0]] = {}
        for curr_property in obj[6].split(","):
            properties_name_contrast[obj[0]][properties_name_invert[curr_property]] = curr_property
    name_zh = dict(zip([obj[0] for obj in entity_result], [obj[1] for obj in entity_result]))
    range_table_zh = {}
    mappoints = {}
    for key in range_table:
        value_list = []
        for obj in range_table[key]:
            if obj in pre_data:
                value_list.append(pre_data[obj])
            else:
                value_list.append(name_zh[obj])
        range_table_zh[key] = value_list
    created_entities = {}
    created_classes = {}
    class_to_id = {}
    id_map_table = {}
    max_id = 1


def set_table(value):
    global_var.range_table = value


def get_graph():
    return global_var.graph


def get_table():
    return global_var.range_table


def get_table_zh():
    return global_var.range_table_zh


def set_created_enetities(value):
    global_var.created_entities = value


def get_created_entities():
    return global_var.created_entities


def set_max_id(value):
    global_var.max_id = value


def get_max_id():
    return global_var.max_id


def set_id_map_table(value):
    global_var.id_map_table = value


def get_id_map_table():
    return global_var.id_map_table


def get_properties_name_invert():
    return global_var.properties_name_invert


def get_properties_name_contrast():
    return global_var.properties_name_contrast


def set_created_classes(value):
    global_var.created_classes = value


def get_created_classes():
    return global_var.created_classes


def get_pre_data():
    return global_var.pre_data


def get_kg_ids():
    return global_var.user_kg_ids


def set_kg_ids(value, key):
    global_var.user_kg_ids[key] = value


def get_mappoints():
    return global_var.mappoints


def set_mappoints(value):
    global_var.mappoints = value


def set_MAP_FLAG(value):
    global_var.MAP_FLAG = value
