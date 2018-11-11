def median(lst):
  lst.sort()
  a = (len(lst) / 2)
  return lst[a]

def mode(lst):
  return max(set(lst), key=lst.count)

def upperQuart(lst):
  lst.sort()   
  a = ((3 * len(lst)) / 4)
  return lst[a]

def lowerQuart(lst):
  lst.sort()
  a = (len(lst) / 4)
  return lst[a]
