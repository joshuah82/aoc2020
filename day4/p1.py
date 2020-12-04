#!/usr/bin/python3
import sys, re

REQ_FIELDS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
OPT_FIELEDS = ('cid')

with open(f'{sys.path[0]}/day4.txt', 'r') as f:
    batch = f.read()

field_pattern = '\w{3}:[#\w\d]+'
entry_pattern = f'^({field_pattern}\s?)+'

valid_entries = 0
for group in re.finditer(entry_pattern, batch, re.M):
    entry = group.group(0).strip()

    missing_fields = False
    for field in REQ_FIELDS:
        if f'{field}:' not in entry:
            missing_fields = True
            break

    if not missing_fields:
        valid_entries += 1

print(f'Answer: {valid_entries}')
