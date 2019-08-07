import argparse
import json
from pathlib import Path
import random
import sys

parser = argparse.ArgumentParser()

parser.add_argument('-o', '--output', type=str, help='')
parser.add_argument('-c', '--count', type=int, help='')
parser.add_argument('-min', '--lower-bound', type=int, help='')
parser.add_argument('-max', '--upper-bound', type=int, help='')

group = parser.add_mutually_exclusive_group()
group.add_argument('-s', '--generate-sequence', action='store_true')
group.add_argument('-d', '--allow-duplicate', action='store_true')

args = parser.parse_args()

file_name = args.output if args.output else 'sample'
file_path = f'/rdev/python-sort/input/{file_name}.txt'

output_file = Path(file_path)
if output_file.is_file():
    print('Output file already exist, it will be overwriten')


lower_bound = args.lower_bound if args.lower_bound else 0
upper_bound = args.upper_bound if args.upper_bound else 9

if lower_bound > upper_bound:
    lower_bound, upper_bound = upper_bound, lower_bound

bound = upper_bound - lower_bound + 1
count = args.count if args.count and args.count < bound else bound


output = []
if args.generate_sequence:
    print(f'Listing sequence from {lower_bound} to {upper_bound}')
    for num in range(lower_bound, upper_bound + 1):
        output.append(num)
    print(*output)

elif args.allow_duplicate:
    print(f'Randomly generate {count} integers between {lower_bound} and {upper_bound}')
    for i in range(count):
        output.append(random.randint(lower_bound, upper_bound))
    print(*output)

elif count == bound:
    print(f'Shuffling integers range from {lower_bound} to {upper_bound}')
    for num in range(lower_bound, upper_bound + 1):
        output.insert(random.randint(0, len(output)), num)
    print(*output)
else:
    print(f'Randomly generate {count} integers between {lower_bound} and {upper_bound} (no duplicate)')
    s = {}
    for i in range(count):
        r = random.randint(lower_bound, upper_bound)
        while r in s:
            r = random.randint(lower_bound, upper_bound)
        output.append(r)
    print(*output)

f = open(file_path, 'w')
json.dump(output, f)

f.close()
