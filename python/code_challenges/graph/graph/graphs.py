from queue import *
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
        v = Vertix(value)
        self.adjacency_list[v] = []
        return v

    def add_edge(self, start_node, end_node, weight=0):
        if start_node not in self.adjacency_list:
            raise KeyError('Start node is not exist in Graph')

        if end_node not in self.adjacency_list:
            raise KeyError('End node is not exist in Graph')

        edge = Edge(end_node, weight)
        self.adjacency_list[start_node].append(edge)

    def get_nodes(self):

        return self.adjacency_list.keys()

    def get_neighbors(self, node):

        return self.adjacency_list[node]

    def size(self):

        return len(self.adjacency_list)

    def __str__(self):
        output = ''
        for vertix in self.adjacency_list.keys():
            output += vertix.value
            for edge in self.adjacency_list[vertix]:
                output += ' -> ' + edge.vertix.value
            output += '\n'
        return output

    def breadth_first(self, node):
        node_lst = []
        queue = Queue()
        visit_node = set()

        if node not in self.adjacency_list or self.adjacency_list[node] == []:
            return None

        queue.enqueue(node)
        visit_node.add(node.value)

        while not queue.isEmpty():
            vertix = queue.dequeue()
            node_lst.append(vertix.value)

            for edge in self.adjacency_list[vertix]:
                if edge.node.value not in visit_node:
                    visit_node.add(edge.node.value)
                    queue.enqueue(edge.node)

        return node_lst


if __name__ == '__main__':
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    graph.add_edge(a, c)
    graph.add_edge(a, d)
    graph.add_edge(b, c)
    graph.add_edge(b, f)
    graph.add_edge(c, a)
    graph.add_edge(c, b)
    graph.add_edge(c, e)
    graph.add_edge(d, a)
    graph.add_edge(d, e)
    graph.add_edge(e, c)
    graph.add_edge(e, d)
    graph.add_edge(e, f)
    graph.add_edge(f, b)
    graph.add_edge(f, e)

    print(graph)
