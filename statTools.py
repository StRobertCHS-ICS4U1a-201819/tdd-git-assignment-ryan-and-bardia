'''
def mean(mylist):
    count = 0
    sum = 0
    for elem in mylist:
        sum += elem
        count += 1
    return round(sum/count,2)
'''
'''
def range(mylist):
    least = min(mylist)
    greatest = max(mylist)
    return (greatest - least)
'''

def variance(mylist):
    count = 0
    firstsum = 0
    secondsum = 0
    for elem in mylist:
        firstsum += elem
        count += 1
    mean = firstsum/count
    for elem in mylist:
        secondsum += (mean-elem)**2
    return round(secondsum/count,2)
