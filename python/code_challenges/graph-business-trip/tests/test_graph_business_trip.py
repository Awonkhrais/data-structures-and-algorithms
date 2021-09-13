from graph_business_trip import __version__
from graph_business_trip.graphb import *

def test_version():
    assert __version__ == '0.1.0'

def test_one():
    test = Graph()
    ## add node
    test.add_node('Amman')
    test.add_node('Irbid')
    test.add_node('Aqaba')
    test.add_node('Zarqa')
    ## add edge
    test.add_edge('Amman','Irbid',150)
    test.add_edge('Amman','Aqaba',82)
    test.add_edge('Irbid','Amman',150)
    test.add_edge('Irbid','Aqaba',99)
    test.add_edge('Aqaba','Amman',82)
    test.add_edge('Aqaba','Irbid',99)
    test.add_edge('Aqaba','Zarqa',37)
    test.add_edge('Zarqa','Aqaba',37)
    assert business_trip(test,['Amman','Aqaba'])==[True, 82]


def test_two():
    test = Graph()
    ## add node
    test.add_node('Amman')
    test.add_node('Irbid')
    test.add_node('Aqaba')
    test.add_node('Zarqa')
    ## add edge
    test.add_edge('Amman','Irbid',150)
    test.add_edge('Amman','Aqaba',82)
    test.add_edge('Irbid','Amman',150)
    test.add_edge('Irbid','Aqaba',99)
    test.add_edge('Aqaba','Amman',82)
    test.add_edge('Aqaba','Irbid',99)

    assert business_trip(test,['Aqaba','Zarqa'])==[False,0]
