from graph import __version__
from graph.graphs import *

def test_version():
    assert __version__ == '0.1.0'

def test_add_vertix():

    graph = Graph()
    actual = graph.add_node('a').value
    expected = 'a'
    assert actual == expected


def test_add_edge():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    graph.add_edge(a, b)
    assert True


def test_get_nodes():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    expected = 2
    actual = len(graph.get_nodes())
    assert actual == expected

# def test_get_neighbors():
#     graph = Graph()
#     a = graph.add_node('a')
#     b = graph.add_node('b')
#     graph.add_edge(a, b)
#     expected = [(b, 0)]
#     actual = graph.get_neighbors(a)
#     assert actual == expected

def test_graph_size():
    graph = Graph()
    actual = graph.size()
    expected = 0
    assert actual == expected

def test_size_empty():
    graph = Graph()
    expected = 0
    actual = graph.size()
    assert actual == expected
