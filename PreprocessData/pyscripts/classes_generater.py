import os
from PreprocessData.database_op import datasql
from pandas._libs import json


class CreatClass(object):
    def __init__(self):
        self.json_path = r'..\all_class_json'
        self.files_path = r'..\all_class_files'
        self.append_content = ""
        self.prefix_property_set = {}

    def creat_class(self, entity_name, information):
        filepath = os.path.join(self.files_path, '{}.py'.format(entity_name))
        if os.path.exists(filepath) is True:
            print("{}已经存在.".format(entity_name))
            return
        self.append_content = ""
        all_properties = self.prefix_property_set[entity_name]  # 包括父类属性
        self_properties = information["property_name"]  # 该类的所有属性
        tab = 4 * " "
        super_names = information['_super']
        for super_name in super_names.split(','):
            self.append_content += 'from PreprocessData.all_class_files.{} import {}\n'.format(
                super_name, super_name)
        self.append_content += 'import global_data\n\n\n'
        class_name = "class {}({}):\n".format(entity_name, super_names)
        self_init_function = 1 * tab
        self_init_function += "def __init__(self"
        self_sentence = ""  # self.property_A = property_A
        for obj in all_properties:
            self_init_function += ", {}=None".format(obj)
        self_init_function += "):\n"
        super_init_function = ""
        if entity_name != "Thing":
            for super_name in super_names.split(','):
                super_init_sentence = 2 * tab + "{}.__init__(self".format(super_name)
                for super_property in self.prefix_property_set[super_name]:
                    super_init_sentence += ", {}".format(super_property)
                super_init_sentence += ")\n"
                super_init_function += super_init_sentence
        self.append_content += class_name + self_init_function + super_init_function
        if len(self_properties) != 0:
            for obj in self_properties:
                self_sentence += 2 * tab + "self.{} = {}\n".format(obj, obj)
            self_properties_init = self_sentence
            self.append_content += self_properties_init + "\n"
            for obj in self_properties:
                self.append_content += 1 * tab + "def set_{}(self, {}):\n".format(obj, obj)
                self.append_content += 2 * tab + "self.{} = {}\n\n".format(obj, obj)
                self.append_content += 1 * tab + "def get_{}(self):\n".format(obj)
                self.append_content += 2 * tab + "return self.{}\n\n".format(obj, obj)
            property_check = '''
    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
'''
            self.append_content += property_check
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(self.append_content)
            f.close()

    def filter_information(self):
        msql = datasql()
        entities = msql.query('entity_tab')
        name_list, prefix_properties = [x[0] for x in entities], [x[6].split(',') for x in entities]
        self.prefix_property_set = dict(zip(name_list, prefix_properties))
        suc_cnt = 0
        fail_cnt = 0
        for element in entities:
            filename = element[0]
            information = {}
            information['nameZh'] = element[1]
            information['_super'] = element[2]
            information["descriptionZh"] = element[4]
            if len(element[5]) == 0:
                information["property_name"] = []
            else:
                information["property_name"] = element[5].split(',')
            try:
                self.creat_class(filename, information)
                suc_cnt = suc_cnt + 1
            except Exception as e:
                print(e)
                fail_cnt = fail_cnt + 1
                print("{} is failed!".format(filename))
        print("总计完成{}个".format(suc_cnt))
        print("失败{}个".format(fail_cnt))


if __name__ == '__main__':
    creat = CreatClass()
    creat.filter_information()
