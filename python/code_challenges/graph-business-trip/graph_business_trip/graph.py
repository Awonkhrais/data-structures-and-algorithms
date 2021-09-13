class Vertix:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertix, weight):
        self.vertix = vertix
        self.weight = weight


class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        vertex  = Vertix(value)
        self.adjacency_list[vertex ] = []
        return vertex

    def add_edge(self, start_node, end_node, weight=0):
        edge = Edge(end_node, weight)
        self.adjacency_list[start_node].append(edge)

    def get_nodes(self):

        return self.adjacency_list.keys()

    def get_neighbors(self, node):

        return self.adjacency_list[node]

    def size(self):

        return len(self.adjacency_list)
