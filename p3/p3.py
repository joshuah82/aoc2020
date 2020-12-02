#!/usr/bin/python3
import sys, re

with open(f'{sys.path[0]}/p3.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

valid = 0
pattern = '(\d+)-(\d+) (\w): (\w+)'

for line in lines:
    match = re.search(pattern, line)

    imin = int(match.group(1))
    imax = int(match.group(2))
    letter = match.group(3)
    password = match.group(4)
    occurences = password.count(letter)

    if occurences >= imin and occurences <= imax:
        valid += 1

print(f'Answer: {valid}')
