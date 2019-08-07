import argparse
import json
import sys
from pathlib import Path
from sty import fg

def swap(input, x, y):
    input[x], input[y] = input[y], input[x]

def print_list(input, x, y):
    if x > y:
        x, y = y, x
    print(*input[:x], fg(201) + str(input[x]) + fg.rs, *input[x+1:y], fg(201) + str(input[y]) + fg.rs, *input[y+1:])

def bubble_sort(input):
    n = len(input)
    iteration, comparison, exchange = 0, 0, 0
    swapped = True
    while swapped:
        swapped = False
        iteration += 1
        print(f'Iteration: {iteration}')
        for i in range(n - 1):
            comparison += 1
            if input[i] > input[i + 1]:
                exchange += 1
                swap(input, i, i + 1)
                print_list(input, i, i + 1)
                swapped = True
        n -= 1
    return [iteration, comparison, exchange]

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, help='file containing white-space delimited integers')
args = parser.parse_args()

file_name = args.input if args.input else 'sample'
file_path = f'/rdev/python-sort/input/{file_name}.txt'

input_file = Path(file_path)
if not input_file.is_file():
    print('Input file does not exist')
    sys.exit()

f = open(file_path, 'r')
input_data = []

# fl = f.readlines()
# for line in fl:
#     input_data += line.split()
input_data = json.load(f)

f.close()

print('Algorithm: Bubble sort\n')

print('Input:')
print(*input_data, '\n')

stats = bubble_sort(input_data)

print('\nResult:')
print(*input_data)

print(f'''
Iteration: {stats[0]}
Comparison: {stats[1]}
Swapped: {stats[2]}''')
