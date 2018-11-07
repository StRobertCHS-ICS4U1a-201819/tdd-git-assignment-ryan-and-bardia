def mean(mylist):
    count = 0
    sum = 0
    for elem in mylist:
        sum += elem
        count += 1
    return round(sum/count,2)