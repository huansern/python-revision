import argparse
import json
from pathlib import Path
import os
import sys

from sorting.algorithm import bubble, insertion, selection


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, help='text file containing white-space delimited integers')
parser.add_argument('-a', '--algorithm', type=str, help='')
args = parser.parse_args()

file_name = args.input if args.input else 'sample.txt'
dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = f'{dir_path}/input/{file_name}'

input_file = Path(file_path)
if not input_file.is_file():
    print('Input file does not exist')
    sys.exit()

with open(file_path, 'r') as f:
    input_data = json.load(f)

if args.algorithm == 'insertion':
    algorithm = insertion
elif args.algorithm == 'selection':
    algorithm = selection
else:
    algorithm = bubble


print(f'Algorithm: {algorithm.__name__}\n\nInput:')
print(*input_data, '\n')

algorithm.sort(input_data)

print('\nResult:')
print(*input_data)
