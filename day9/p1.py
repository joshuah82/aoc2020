#!/usr/bin/python3
import sys

BLOCK_SIZE = 25

with open(f'{sys.path[0]}/day9.txt', 'r') as f:
    lines = [int(line.strip()) for line in f.readlines()]

bad_num = -1
for idx in range(0, len(lines) - 1):
    target_num = lines[idx + BLOCK_SIZE]
    block = lines[idx:idx + BLOCK_SIZE]

    found_match = False
    for first_idx, first_num in enumerate(block):
        for second_num in block[first_idx + 1:]:
            if first_num + second_num == target_num:
                found_match = True
                break

        if found_match == True:
            break

    if found_match == False:
        bad_num = target_num
        print(f'Answer: {bad_num}')
        exit()

