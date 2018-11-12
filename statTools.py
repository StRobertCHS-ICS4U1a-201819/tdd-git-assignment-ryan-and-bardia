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
'''