#!/usr/bin/python3
import sys, math

MOVE_R = 3
MOVE_D = 1

with open(f'{sys.path[0]}/day3.txt', 'r') as f:
    pattern_lines = [pattern_line.strip() for pattern_line in f.readlines()]

pattern_width = len(pattern_lines[0])
pattern_height = len(pattern_lines)
required_width = math.ceil((pattern_height / MOVE_D) * MOVE_R)
pattern_iterations = math.ceil(required_width / pattern_width)

full_pattern = []
for line in pattern_lines:
    full_pattern.append(line * pattern_iterations)

loc = {'x' : 0, 'y' : 0}
found_trees = 0
while loc['y'] < pattern_height:
    if full_pattern[loc['y']][loc['x']] == '#':
        found_trees += 1

    loc['x'] += MOVE_R
    loc['y'] += MOVE_D

print(f'Answer: {found_trees}')
