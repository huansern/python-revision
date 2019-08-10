from sorting.common import util

def sort(data, visible = True):
    '''Sort a list of integers using bubble sort algorithm
    '''

    swapped, n = True, len(data)
    while swapped:
        swapped = False

        for i in range(n - 1):
            if data[i] > data[i + 1]:
                util.swap(data, i, i + 1, visible)
                swapped = True

        n -= 1

    return data
