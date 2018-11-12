from statTools import*
import pytest
def test_median1():
  assert (median([100, 9, 3, 5, 4, 8, 16, 2, 6]) == 6)
def test_median2():
  assert (median([-3, 4, 7, 13, 17, -4, -18, 10]) == 7)
def test_median3():
  assert (median([]) == "Error: Empty List.")

def test_mode1():
  assert (mode([4, 1, 14, 5, 7, 43, 5, 11, 22, 1, 5, 58]) == 5)
def test_mode2():
  assert (mode([6, -1, 5, 11, 1, -24, 5, 5, -6, 78, 18, 90]) == 5)
def test_mode3():
  assert (mode([]) == "Error: Empty List.")

def test_upperQuart1():
  assert (upperQuart([1, 4, 3, 8, 6, 17, 11, 44, 25, 18]) == 18)
def test_upperQuart2():
  assert (upperQuart([1, -14, 6, -2, 13, 7, 5, 4]) == 6)
def test_upperQuart3():
  assert (upperQuart([]) == "Error: Empty List.")


def test_lowerQuart1():
  assert (lowerQuart([1, 3, 4, 8, 10, 22, 27, 33, 34, 45, 56]) == 4)
def test_lowerQuart2():
  assert (lowerQuart([1, -14, 6, 13, -1, 4, 14, 2, 7]) == 3)
def test_lowerQuart3():
  assert (lowerQuart([]) == "Error: Empty List.")