def median(lst):
    if len(lst) == 0:
      return "Error: Empty List."
    else:
      lst.sort()
      a = int((len(lst) / 2))
      return lst[a]

def mode(lst):
  if len(lst) == 0:
    return "Error: Empty List."
  else:
    return max(set(lst), key=lst.count)

def upperQuart(lst):
  lst.sort()
  if len(lst) == 0:
    return "Error: Empty List."
  else:
    a = int((3 * len(lst) - 1) / 4)
    return lst[a]

def lowerQuart(lst):
  lst.sort()
  if len(lst) == 0:
    return "Error: Empty List."
  else:
    a = int(len(lst) / 4)
    return lst[a]

