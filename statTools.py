<<<<<<< HEAD
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

def mean(mylist):
    count = 0
    sum = 0
    for elem in mylist:
        if type(elem) != str:
            sum += elem
            count += 1
        else:
            return 'An error has occured. Please enter an integer.'
    if count == 0:
        return 'An error has occured. Please enter an integer.'
    else:
        return round(sum/count,2)

def range(mylist):
    if mylist == False:
        return 'An error has occured. Please enter an integer.'
    else:
        for elem in mylist:
            if type(elem) == str:
                return 'An error has occured. Please enter an integer.'
            else:
                break
        least = min(mylist)
        greatest = max(mylist)
        return (greatest - least)


def variance(mylist):
    count = 0
    firstsum = 0
    secondsum = 0
    for elem in mylist:
        if type(elem) != str:
            firstsum += elem
            count += 1
        else:
            return 'An error has occured. Please enter an integer.'
    if count == 0:
        return 'An error has occured. Please enter an integer.'
    else:
        mean = firstsum/count
        for elem in mylist:
            secondsum += (mean-elem)**2
        return round(secondsum/count,2)


def stnd_deviation(mylist):
    count = 0
    firstsum = 0
    secondsum = 0
    for elem in mylist:
        if type(elem) != str:
            firstsum += elem
            count += 1
        else:
            return 'An error has occured. Please enter an integer.'
    if count == 0:
        return 'An error has occured. Please enter an integer.'
    else:
        mean = firstsum/count
        for elem in mylist:
            secondsum += (mean-elem)**2
        return round((secondsum/count)**0.5,2)

