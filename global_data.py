from django.db.models import Max
from PreprocessData.database_op import datasql


class global_var:
    pre_data = {"NoneType": "空值", "str": "自定义字符串", "int": "整数", "bool": "布尔（真假）", "date": "日期", "float": "非整数"}
    msql = datasql()
    properties_data = msql.query("property_tab")
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
