'''
def mean(mylist):
    count = 0
    sum = 0
    for elem in mylist:
        if type(elem) != str:
            sum += elem
            count += 1
        else:
            return 'An error has occured. Please enter an integer.'
    return round(sum/count,2)
'''
'''
def range(mylist):
    if mylist == False:
        return 'An error has occured. Please enter an integer.'
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
    mean = firstsum/count
    for elem in mylist:
        secondsum += (mean-elem)**2
    return round((secondsum/count)**0.5,2)
'''