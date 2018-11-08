from statTools import*
import pytest

def test_mean1():
    assert (mean([10,10,10,10,10,10,10,10,10,10])==10)
def test_mean2():
    assert (mean([12,432,453,122,324,32,-324,-746,21,-233])==9.3)
def test_mean3():
    assert (mean([4365,-43,-793,4354,31,213,-4233])==556.29)