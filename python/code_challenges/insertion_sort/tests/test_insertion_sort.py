from insertion_sort import __version__
from insertion_sort.insertion_sort import insertion_sort



def test_version():
    assert __version__ == '0.1.0'

def test_insert_sorting():
    actual = insertion_sort([8, 4, 23, 42, 16, 15])
    assert actual == [4, 8, 15, 16, 23, 42]
