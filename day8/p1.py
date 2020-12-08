#!/usr/bin/python3
import sys

with open(f'{sys.path[0]}/day8.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

acc = 0
loc = 0
locs = []
while loc not in locs:
    opr, arg = lines[loc].split()
    locs.append(loc)
    if opr == 'acc':
        acc += eval(arg)
        loc += 1
    elif opr == 'jmp':
        loc += eval(arg)
    elif opr == 'nop':
        loc += 1

print(f'Answer: {acc}')
