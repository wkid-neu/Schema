from datetime import datetime

from py2neo import Graph

from PreprocessData.all_class_files.all_class import *


class TransClass(object):
    def __init__(self, monitor_id, app_name):
        self.graph = global_data.get_graph()
        self.vis = []
        self.result = {}
        self.node_data = {}
        self.id_node_tab = {}
        self.monitor_id = monitor_id
        self.app_name = app_name
        self.properties_name_contrast = global_data.get_properties_name_contrast()
        self.node_dict = {}
        self.kg_ids = {}
        self.entity_class_json = {}
        self.id_class_json = {}
        self.class_to_id = {}
        self.links = []
        self.nodes = []

    def extract_data(self, extract_all):
        if extract_all is False:
            data = self.graph.run(
                "match (a)-[rel]->(b) where a.monitor_id={} and a.app_name='{}' return a,rel,b".format(self.monitor_id,self.app_name)).data()
        else:
            data = self.graph.run(
                "match (a)-[rel]->(b) where a.app_name='{}' return a,rel,b".format(self.app_name)).data()
        return data

    def transfer(self, extract_all=False):
        data = self.extract_data(extract_all)
        for three_tuple in data:
            st_node = three_tuple['a']
            if st_node.identity not in self.id_node_tab:
                self.id_node_tab[st_node.identity] = st_node
            st_node = self.id_node_tab[st_node.identity]
            ed_node = three_tuple['b']
            if ed_node.identity not in self.id_node_tab:
                self.id_node_tab[ed_node.identity] = ed_node
            ed_node = self.id_node_tab[ed_node.identity]
            three_tuple['a'] = st_node
            three_tuple['b'] = ed_node
        node_set = set()
        for three_tuple in data:
            st_node = three_tuple['a']
            rel = three_tuple['rel']
            ed_node = three_tuple['b']
            if self.node_data.get(st_node) is None:
                self.node_data[st_node] = {}
            class_name = dict(st_node)['class_hierarchy'].split(":")[0]
            if self.node_data[st_node].get(self.properties_name_contrast[class_name][list(rel.types())[0]]) is None:
                self.node_data[st_node][self.properties_name_contrast[class_name][list(rel.types())[0]]] = []
            self.node_data[st_node][self.properties_name_contrast[class_name][list(rel.types())[0]]].append(
                ed_node)
            node_set.add(st_node)
            node_set.add(ed_node)
            self.links.append({"source": st_node.identity, "target": ed_node.identity, "type": list(rel.types())[0]})
        data = self.graph.run(
            "match (n) where not (n)–[]-() and n.monitor_id={} return n".format(self.monitor_id)).data()
        for isolated_node in data:
            node = isolated_node['n']
            node_set.add(node)

        for node in node_set:
            info = dict(node)
            info["id"] = node.identity
            info["type"] = ",".join(str(node.labels).split(":")[1:])
            self.nodes.append(info)
            if node in self.node_data:
                continue
            self.node_data[node] = []
        print(self.node_data)
        for obj in self.node_data:
            if obj in self.vis:
                continue
            self.kg_ids[obj.identity] = []
            self.process(obj.identity, obj)

    def process(self, root_node_id, node):
        self.kg_ids[root_node_id].append(node.identity)
        if node in self.vis:
            return
        self.vis.append(node)
        class_ = dict(node)['class_hierarchy'].split(":")[0]

        name = dict(node)['name']
        master = dict(node)['monitor_id']
        if self.entity_class_json.get(class_) is None:
            self.entity_class_json[class_] = []
        if node.identity in self.result:
            return self.result[node.id]
        module_meta = __import__("PreprocessData.all_class_files.all_class", globals(), locals(), [class_])
        class_meta = getattr(module_meta, class_)
        kwargs = {'name': [name]}
        node_properties_list = self.node_data[node]
        for node_property in node_properties_list:
            if kwargs.get(node_property) is None:
                kwargs[node_property] = []
            for value in node_properties_list[node_property]:
                if value in self.node_dict:
                    kwargs[node_property].append(self.node_dict.get(value))
                    continue
                kwargs[node_property].append(self.process(root_node_id, value))
        node_t_class = class_meta(**kwargs)
        if not hasattr(node_t_class, 'node_id'):
            setattr(node_t_class, 'node_id', node.identity)
        self.node_dict[node] = node_t_class
        self.result[node.identity] = {"class": node_t_class, "fill_data": kwargs, "monitor_id": master}
        self.entity_class_json[class_].append({"class": node_t_class, "node_id": node.identity, "name": kwargs['name']})
        return node_t_class
