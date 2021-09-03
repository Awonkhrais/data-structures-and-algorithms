from hash_table import __version__
from hash_table.hash_table import *

def test_version():
    assert __version__ == '0.1.0'


def test_adding():
    test = HashTable()
    test.add('hello',100)
    assert test.contains('hello') == True

def test_get():
    test=HashTable()
    test.add('hello',100)
    assert test.get('hello')==100

def test_return_none():
    test = HashTable()
    test.add('hello',100)
    assert test.get('hi') == None

def test_collision():
    test=HashTable()
    test.add('dog',100)
    test.add('god',1001)
    assert test.get('dog')==100
    assert test.get('god')==1001

def test_hash():  # test 6

    test = HashTable()
    assert test.hash('awon') == 111
