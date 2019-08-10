from sorting.common import util

def sort(data, visible = True):
    '''Sort a list of integers using insertion sort algorithm
    '''

    for i in range(1, len(data)):
        while i > 0 and data[i - 1] > data[i]:
            util.swap(data, i - 1, i, visible)
            i -= 1

    return data
