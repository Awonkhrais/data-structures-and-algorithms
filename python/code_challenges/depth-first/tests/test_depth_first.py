from depth_first import __version__
from depth_first.graph import *
import pytest


def test_version():
    assert __version__ == '0.1.0'


def test_one(): # empty graph
    test = Graph()
    actual = test.depth_first()
    expected = []
    assert actual == expected

def test_two(depth_f):
    actual = []
    for node in depth_f[0].depth_first():
        actual.append(node.value)
    expected = ['Amman', 'Irbid', 'Zarqa', 'Aqaba', 'Petra', 'Salt']
    assert actual == expected


@pytest.fixture
def depth_f():

    test = Graph()
    vertix1 = test.add_node('Amman')
    vertix2 = test.add_node('Irbid')
    vertix3 = test.add_node('Zarqa')
    vertix4 = test.add_node('Aqaba')
    vertix5 = test.add_node('Salt')
    vertix6 = test.add_node('Petra')

    test.add_edge(vertix1, vertix2, 70)
    test.add_edge(vertix1, vertix3, 64)
    test.add_edge(vertix2, vertix3, 125)
    test.add_edge(vertix2, vertix4, 63)
    test.add_edge(vertix3, vertix4, 155)
    test.add_edge(vertix3, vertix5, 250)
    test.add_edge(vertix3, vertix6, 30)
    test.add_edge(vertix4, vertix6, 60)
    test.add_edge(vertix5, vertix6, 40)
    return [test]
