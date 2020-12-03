#!/usr/bin/python3
import sys, math

slopes = [{'r' : 1, 'd' : 1},
          {'r' : 3, 'd' : 1},
          {'r' : 5, 'd' : 1},
          {'r' : 7, 'd' : 1},
          {'r' : 1, 'd' : 2}]

with open(f'{sys.path[0]}/day3.txt', 'r') as f:
    pattern_lines = [pattern_line.strip() for pattern_line in f.readlines()]

answer = 1
for slope in slopes:
    pattern_width = len(pattern_lines[0])
    pattern_height = len(pattern_lines)
    required_width = math.ceil((pattern_height / slope['d']) * slope['r'])
    pattern_iterations = math.ceil(required_width / pattern_width)

    full_pattern = []
    for line in pattern_lines:
        full_pattern.append(line * pattern_iterations)

    loc = {'x' : 0, 'y' : 0}
    found_trees = 0
    while loc['y'] < pattern_height:
        if full_pattern[loc['y']][loc['x']] == '#':
            found_trees += 1

        loc['x'] += slope['r']
        loc['y'] += slope['d']

    answer *= found_trees
    print(f'slope {slope["r"]} x {slope["d"]}: {found_trees}')

print(f'Answer: {answer}')
