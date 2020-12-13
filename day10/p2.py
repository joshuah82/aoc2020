#!/usr/bin/python3
import sys

with open(f'{sys.path[0]}/day10.txt', 'r') as f:
    lines = [int(line.strip()) for line in f.readlines()]

lines.sort()
lines.insert(0, 0)
lines.append(max(lines) + 3)

combo_count = 0
for idx in range(0, len(lines) - 1):
    diff = lines[idx + 1] - lines[idx]
    if diff == 1:
        one_count += 1
    elif diff == 3:
        three_count += 1

print(f'Answer: {one_count * three_count}')
