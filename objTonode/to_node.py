from py2neo import Graph

import global_data


class TransNode(object):
    def __init__(self, monitor_id, app_name=None):
        self.cre_vis = {}
        self.graph = Graph("http://localhost:7474", username="neo4j", password='123123')
        self.upd_vis = []
        self.monitor_id = monitor_id
        self.app_name = app_name
        if app_name == "MapSchema":
            self.markpoint_data = global_data.get_mappoints()

    def update_node(self, update_cypher):
        for obj in update_cypher:
            try:
                self.graph.run(obj)
            except Exception as e:
                print("更改失败", e)

    def to_node(self, obj):
        if obj in self.cre_vis:
            return
        class_name = type(obj).__name__
        attr_value = obj.__dict__
        module_meta = __import__("objTonode.neo_classes", globals(), locals(), [class_name])
        class_meta = getattr(module_meta, class_name)
        kwargs = {}
        if attr_value.get("name") is not None:
            kwargs["name"] = attr_value.get("name")[0]
            kwargs["monitor_id"] = self.monitor_id
            kwargs["app_name"] = self.app_name
        neo_node = class_meta(**kwargs)
        class_hierarchy_list = neo_node.inherited_labels()
        neo_node.class_hierarchy = ':'.join(class_hierarchy_list)
        neo_node.save()
        for key in attr_value:
            value_list = attr_value.get(key)
            if key == 'node_id' or key == 'name' or key == 'app_name' or value_list is None or len(value_list) == 0:
                continue
            for value in value_list:
                if value in self.cre_vis:
                    val_node = self.cre_vis[value]
                else:
                    val_node = self.to_node(value)
                if val_node is not None:
                    getattr(neo_node, key).connect(val_node)
        self.cre_vis[obj] = neo_node
        return neo_node
