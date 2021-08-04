from datetime import datetime
from py2neo import Graph
from PreprocessData.all_class_files.all_class import *

graph = Graph("http://localhost:7474", username="neo4j", password='123123')

data = graph.run("match (n) where n.monitor_id=2 return n").data()
for obj in data:
    node = obj['n']
    print(node.labels)
    print(list(node.labels))