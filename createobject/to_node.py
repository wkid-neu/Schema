from createobject.neo_classes import Text
from PreprocessData.all_class_files.all_class import Person
from createobject import to_class
from django.conf import settings


class TransNode(object):
    def __init__(self, monitor_id):
        self.vis = {}
        self.monitor_id = monitor_id
        self.common_properties = {'str': 'Text', 'int': 'Integer', 'float': 'Float', 'bool': 'Bool', 'date': 'Date'}

    def to_node(self, obj):
        if obj in self.vis:
            return
        class_name = type(obj).__name__
        attr_value = obj.__dict__
        module_meta = __import__("createobject.neo_classes", globals(), locals(), [class_name])
        class_meta = getattr(module_meta, class_name)
        kwargs = {}
        if attr_value.get("name") is not None:
            kwargs["name"] = attr_value.get("name")[0]
            kwargs["monitor_id"] = self.monitor_id
        neo_node = class_meta(**kwargs)
        neo_node.save()
        for key in attr_value:
            value_list = attr_value.get(key)
            if key == 'node_id' or key == 'name' or value_list is None or len(value_list) == 0:
                continue
            for value in value_list:
                if type(value).__name__ in self.common_properties:
                    common_class_name = self.common_properties[type(value).__name__]
                    common_module_meta = __import__("createobject.neo_classes", globals(), locals(),
                                                    [common_class_name])
                    common_class_meta = getattr(common_module_meta, common_class_name)
                    val_node = common_class_meta(name=value, monitor_id=self.monitor_id)
                    val_node.save()
                else:  # if cur_node  exits ,contniue
                    if value in self.vis:
                        val_node = self.vis[value]
                    else:
                        val_node = self.to_node(value)
                if val_node is not None:
                    getattr(neo_node, key).connect(val_node)
        self.vis[obj] = neo_node
        return neo_node
