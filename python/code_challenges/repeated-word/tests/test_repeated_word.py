from repeated_word import __version__
from repeated_word.repeated_word import *

def test_version():
    assert __version__ == '0.1.0'

def test_repeted_Word():
    test=HashTable()
    assert test.word_repeated("Once upon a time, there was a brave princess who...")== "a"

def test_no_repeted_Word():
    test=HashTable()
    assert test.word_repeated("My name is Awon")== "No repeated words"
