import json
import os
from PreprocessData.database_op import datasql
from PreprocessData.all_class_files.all_class import *

all_subclasses = {}


class FindPrefixProperties(object):
    def __init__(self, entity_info):
        self.entity_info = entity_info
        self.vis = []
        self.entity_dict = {}
        self.prefix_property_set = {}

    def dfs(self, pro_entity):
        self.vis.append(pro_entity)
        if len(self.entity_dict[pro_entity][5]) == 0:
            prefix_property = []
        else:
            prefix_property = self.entity_dict[pro_entity][5].split(',')
        if pro_entity == "Thing":
            self.prefix_property_set[pro_entity] = prefix_property
            return prefix_property
        fathers = self.entity_dict[pro_entity][2].split(',')
        temp_list = []
        for obj in fathers:
            result = self.dfs(obj)
            for value in result:
                if value not in temp_list:
                    temp_list.append(value)
        for obj in prefix_property:
            if obj not in temp_list and obj != '':
                temp_list.append(obj)
        self.prefix_property_set[pro_entity] = temp_list
        return temp_list

    def find_prefix_property(self):
        name_list = [x[0] for x in self.entity_info]
        self.entity_dict = dict(zip(name_list, self.entity_info))
        for obj in name_list:
            if obj not in self.vis:
                self.dfs(obj)


class FindRelative(object):
    def __init__(self, content):
        self.content = content
        self.result = {}
        self.vis = []  # 该实体是否出现过

    def solve(self, obj, father):
        if obj['name'] in self.vis:
            self.result[obj['name']][2].add(father)
        else:
            self.result[obj['name']] = [obj['name'], obj['nameZh'], {father},
                                        "http://cnschema.org/data/{}.json".format(obj['name'])]
            self.vis.append(obj['name'])
        if obj.get("children") is None:
            return
        for element in obj['children']:
            self.solve(element, obj['name'])


def find_property(entity_name, content):
    result = ""
    pro_content = content['_pTree']
    for obj in pro_content:
        if obj["rdfs:label"] == entity_name:  # ptree里面包含自己和所有父类，要过滤出自己的
            for value in obj['_properties']:
                result += value["rdfs:label"] + ','
            return result[0:-1]
    return result


def process_class():
    msql = datasql()
    with open(r"../processing_files/classes.json", "r", encoding="utf-8") as f:
        temp_json = f.read()
    content = json.loads(temp_json)
    f.close()
    find_relative = FindRelative(content)
    find_relative.solve(find_relative.content, "object")
    entity_info = []
    for key in find_relative.result:
        obj = find_relative.result[key]
        str = ''
        for element in obj[2]:
            str += element + ','
        obj[2] = str[0:-1]
        with open(r"../all_class_json/{}.json".format(obj[0]), 'r', encoding='utf-8') as f:
            read_data = json.loads(f.read())
            properties = find_property(obj[0], read_data)
            obj.append(read_data['descriptionZh'])
            obj.append(properties)
            entity_info.append(obj)
            f.close()
    find_prefix = FindPrefixProperties(entity_info)
    find_prefix.find_prefix_property()
    for i in range(len(entity_info)):
        entity_info[i].append(",".join(find_prefix.prefix_property_set[entity_info[i][0]]))
    msql.insert_class_info(entity_info)
    msql.close()


def process_property():
    msql = datasql()
    with open(r"../processing_files/properties.json", "r", encoding="utf-8") as f:
        temp_json = f.read()
    content = json.loads(temp_json)
    f.close()
    result = []
    for obj in content:
        if obj["rdfs:label"] == 'yield':
            obj["rdfs:label"] = 'yielded'
        result.append([obj["rdfs:label"], obj["nameZh"], "http://cnschema.org/data/{}.json".format(obj["rdfs:label"]),
                       obj["descriptionZh"]])
    msql.insert_property_info(result)
    msql.close()


def get_all_classes(model):
    subclass_list = []
    for subclass in model.__subclasses__():
        subclass_list.append(subclass.__name__)
        if all_subclasses.get(subclass.__name__) is None:
            son_subclasses = get_all_classes(subclass)
        else:
            son_subclasses = all_subclasses.get(subclass.__name__)
        for obj in son_subclasses:
            if obj not in subclass_list:
                subclass_list.append(obj)
    all_subclasses[model.__name__] = subclass_list
    return subclass_list


def extra_range(path):
    msql = datasql()
    result = msql.query('entity_tab')
    cls = []
    se = set()
    for obj in result:
        cls.append(obj[0])
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                temp_content = f.read()
                content = json.loads(temp_content)
                for obj in content["rangeIncludes"]:
                    se.add(obj["rdfs:label"])
        except Exception as e:
            print("{}失败".format(file))
    for obj in se:
        if obj not in cls:
            print(obj)


def process_range():
    get_all_classes(Thing)
    msql = datasql()
    path = r"..\all_property_json"
    result = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                temp_content = f.read()
                content = json.loads(temp_content)
                name = content["_node_label"]
                cls = ['NoneType']
                for obj in content["rangeIncludes"]:
                    type = obj["rdfs:label"]
                    if type == "Text" or type.lower() == "url":
                        type = "str"
                    elif type == "Integer" or type == "Number":
                        type = "int"
                    elif type == "Boolean":
                        type = 'bool'
                    elif type == "Date" or type == "DateTime" or type == "Time":
                        type = 'date'
                    else:
                        for val in all_subclasses.get(type):
                            cls.append(val)
                    if type not in cls:
                        cls.append(type)
                    if type == "Number":
                        cls.append("float")
                result.append([name, ",".join(cls)])
        except Exception as e:
            print("{}失败！".format(name), e)
    msql.insert_range_tab(result)
    msql.close()


if __name__ == "__main__":
    # process_class()
    # process_property()
    process_range()
