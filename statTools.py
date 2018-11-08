
def mean(mylist):
    count = 0
    sum = 0
    for elem in mylist:
        sum += elem
        count += 1
    return round(sum/count,2)
'''
def range(mylist):
    min_value = None
    for value in mylist:
        if not min_value:
            min_value = value
        elif value < min_value:
            min_value = value
    return min_value
'''