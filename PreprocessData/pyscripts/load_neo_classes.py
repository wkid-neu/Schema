import os
from PreprocessData.database_op import datasql
import global_data


class TransNeoClasses(object):
    def __init__(self, preprocess_data, properties_nameZh):
        self.common_properties = {'str': 'Text', 'int': 'Integer', 'float': 'Float', 'bool': 'Bool', 'date': 'Date'}
        self.preprocess_data = preprocess_data
        self.properties_nameZh = properties_nameZh
        self.file_path = r"../../createobject/neo_classes.py"
        self.vis = ['object']
        self.result = ""
        self.range_table = global_data.get_table()
        self.head = '''
from django_neomodel import DjangoNode
from neomodel import (config, StructuredNode, Property, StringProperty, IntegerProperty,
                      UniqueIdProperty, BooleanProperty, DateProperty, DateTimeProperty,
                      ArrayProperty, JSONProperty, FloatProperty, RelationshipTo, RelationshipFrom)
from createobject.set_relationship import create_relationship_to,create_relationship_from,create_relationship

config.DATABASE_URL = 'bolt://neo4j:123123@localhost:7687'


class Meta:
    app_label = 'createobject'\n\n
'''
        self.tail = '''
class Text(Thing):
    pass
  
  
class Date(Thing):
    pass
    
    
class Bool(Thing):
    pass
    

class Integer(Thing):
    pass


class Float(Thing):
    pass  
'''

    def get_property_data(self, property):
        property_range = self.range_table.get(property)
        pre_add_values = []

        if property_range is not None:
            for value in property_range:
                if value == 'NoneType':
                    continue
                if value in self.common_properties:
                    value = self.common_properties[value]
                if value not in pre_add_values:
                    pre_add_values.append(value)
        return pre_add_values

    def process(self):
        self.result += self.head
        tab = 4 * " "
        flag = False
        while len(self.vis) < len(self.preprocess_data):
            for obj in self.preprocess_data:
                entity_name = obj[0]
                temp_data = ""
                super_names = obj[1]
                if entity_name in self.vis:
                    continue
                for father in super_names.split(','):
                    if father not in self.vis:
                        flag = True
                        continue
                if flag is True:
                    flag = False
                    continue
                self.vis.append(entity_name)
                entity_properties = obj[2].split(',')
                if super_names == 'object':
                    super_names = 'DjangoNode'
                temp_data += "class {}({}):\n".format(entity_name, super_names)
                if entity_properties[0] == '':
                    self.result += temp_data
                    self.result += 1 * tab + "pass\n\n\n"
                    continue
                for property in entity_properties:
                    if property == 'name':
                        temp_data += 1 * tab + "name = StringProperty()\n\n"
                        temp_data += 1 * tab + "monitor_id = IntegerProperty()\n\n"
                        continue
                    pre_add_values = self.get_property_data(property)
                    temp_data += 1 * tab + "{} = create_relationship_to({}, {})\n\n".format(property, pre_add_values,
                                                                                            '\'{}\''.format(
                                                                                                self.properties_nameZh.get(
                                                                                                    property)))
                self.result += temp_data + "\n"
        self.result += self.tail
        with open(self.file_path, 'w', encoding='utf-8') as f:
            f.write(self.result)
            f.close()


if __name__ == "__main__":
    msql = datasql()
    entities = msql.query('entity_tab')
    properties = msql.query('property_tab')
    properties_nameZh = dict(zip([obj[0] for obj in properties], [obj[1] for obj in properties]))
    preprocess_data = [[obj[0], obj[2], obj[5]] for obj in entities]  # 实体名，实体父类们，实体自己的属性
    transer = TransNeoClasses(preprocess_data, properties_nameZh)
    transer.process()
