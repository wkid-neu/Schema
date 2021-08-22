from py2neo import Graph


def delete_kg(ids):
    graph = Graph("http://localhost:7474", username="neo4j", password='123123')
    graph.run("match (n) where id(n) in {} detach delete n".format(ids))
