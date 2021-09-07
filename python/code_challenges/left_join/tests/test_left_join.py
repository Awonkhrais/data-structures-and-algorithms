from left_join import __version__
from left_join.leftjoin import *
from left_join.hashtabel import *


def test_version():
    assert __version__ == '0.1.0'

def test_one():
  data1=HashTable()
  data1.add('fond','enamored')

  data2=HashTable()
  data2.add('fond','averse')
  assert left_join(data1,data2)==[['fond', 'enamored', 'averse']]


def test_two():
  data1=HashTable()
  data1.add('fond','enamored')

  data2=HashTable()
  data2.add('warth','anger')
  assert left_join(data1,data2)==[['fond', 'enamored', None]]

def test_three():
  data1=HashTable()

  data2=HashTable()
  data2.add('warth','anger')
  assert left_join(data1,data2)==[]

