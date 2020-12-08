#!/usr/bin/python3
import sys, copy

with open(f'{sys.path[0]}/day8.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

def run_sim(lines):
    acc = 0
    loc = 0
    locs = []
    while loc not in locs:
        try:
            opr, arg = lines[loc].split()
        except:
            break

        locs.append(loc)
        if opr == 'acc':
            acc += eval(arg)
            loc += 1
        elif opr == 'jmp':
            loc += eval(arg)
        elif opr == 'nop':
            loc += 1

    return loc, acc

exit_acc = 0
exit_loc = 0
test_loc = 0
while exit_loc != len(lines):
    test_lines = copy.deepcopy(lines)
    if test_lines[test_loc].startswith('jmp'):
        test_lines[test_loc] = test_lines[test_loc].replace('jmp', 'nop')
    elif test_lines[test_loc].startswith('nop'):
        test_lines[test_loc] = test_lines[test_loc].replace('nop', 'jmp')

    exit_loc, exit_acc = run_sim(test_lines)
    test_loc += 1

print(f'Answer: {exit_acc}')
