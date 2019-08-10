from sorting.common import util

def sort(data, visible = True):
    '''Sort a list of integers using selection sort:
    '''

    for i in range(0, len(data) - 1):
        minimum = i
        for j in range(i + 1, len(data)):
            if data[j] < data[minimum]:
                minimum = j
        util.swap(data, i, minimum, visible)

    return data

def double_ended_sort(data, visible = True):
    '''Sort a list of integers using double ended selection sort:
    '''

    start, length = 0, len(data)
    while length - start * 2 > 1:
        minimum, maximum, end = start, start, length - 1 - start
        for i in range(start + 1, end + 1):
            if data[minimum] > data[i]:
                minimum = i
            elif data[i] > data[maximum]:
                maximum = i

        if minimum == end and maximum == start:
            # Swapping minimum and maximum value pair
            util.swap(data, maximum, minimum)
        else:
            util.swap(data, start, minimum)
            if maximum == start:
                # Maximum value has been moved to the minimum value originally were
                maximum = minimum
            util.swap(data, maximum, end)

        start += 1

    return data
