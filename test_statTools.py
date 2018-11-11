from statTools import*
import pytest
def test_median1():
  assert (median([10,10,10,10,10,10,10,10,10,10]) == 10)
def test_median2():
  assert (median([100, 9, 3, 6, 5, 4, 8, 16, 2]) == 6)
def test_median3():
  assert (median([2, 3, 4, 5, 7, 7, 7, 16, 9, 100]) == 7)

test_median1()
test_median2()
test_median3()
