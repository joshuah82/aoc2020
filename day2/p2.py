#!/usr/bin/python3
import sys, re

with open(f'{sys.path[0]}/day2.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

valid = 0
pattern = '(\d+)-(\d+) (\w): (\w+)'

for line in lines:
    match = re.search(pattern, line)

    pos1 = int(match.group(1))
    pos2 = int(match.group(2))
    letter = match.group(3)
    password = match.group(4)

    letters = password[pos1-1] + password[pos2-1]
    if letters.count(letter) == 1:
        valid += 1

print(f'Answer: {valid}')
