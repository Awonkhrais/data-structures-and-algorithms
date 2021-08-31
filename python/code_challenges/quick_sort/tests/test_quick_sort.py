from quick_sort import __version__

from quick_sort.quick_sort import quick_sort

def test_version():
    assert __version__ == '0.1.0'


def test_check_QuickSort():

    a=[8, 4, 23, 42, 16, 15]
    actual=quick_sort(a,0,len(a)-1)

    assert [4, 8, 15, 16, 23, 42] == actual
