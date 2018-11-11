def median(lst):
  lst.sort()
  a = int((len(lst) / 2))
  return lst[a]
'''

def upperQuart(lst):
  lst.sort()   
  a = ((3 * len(lst)) / 4)
  return lst[a]

def lowerQuart(lst):
  lst.sort()
  a = (len(lst) / 4)
  return lst[a]
  '''
