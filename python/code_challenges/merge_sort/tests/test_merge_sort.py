from merge_sort import __version__
from merge_sort.merge_sort import merge_sort

def test_version():
    assert __version__ == '0.1.0'

def test_merge_sorting():
    actual = merge_sort([8, 4, 23, 42, 16, 15])
    assert actual == [4, 8, 15, 16, 23, 42]
