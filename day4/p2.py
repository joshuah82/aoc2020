#!/usr/bin/python3
import sys, re

REQ_FIELDS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
OPT_FIELEDS = ('cid')

with open(f'{sys.path[0]}/day4.txt', 'r') as f:
    batch = f.read()

field_pattern = '\w{3}:[#\w\d]+'
entry_pattern = f'^({field_pattern}\s?)+'
valid_pattern = '^(?:byr:(?:19[2-9][0-9]|200[0-2])|iyr:(?:20(?:1[0-9]|20))|eyr:(?:20(?:2[0-9]|30))|hgt:(?:1(?:5[3-9]|[4-8][0-9]|9[0-3])cm|(?:59|6[0-9]|7[0-6])in)|hcl:#[0-9a-f]{6}|ecl:(?:amb|blu|brn|gry|grn|hzl|oth)|pid:\d{9}|cid:\d+)$'

valid_entries = 0
for group in re.finditer(entry_pattern, batch, re.M):
    entry = group.group(0).strip()

    missing_fields = False
    for field in REQ_FIELDS:
        if f'{field}:' not in entry:
            missing_fields = True
            break

    if missing_fields:
        continue

    valid_fields = True
    for field in re.split('\s', entry):
        if re.match(valid_pattern, field) is None:
            valid_fields = False
            break

    if valid_fields:
        valid_entries += 1

print(f'Answer: {valid_entries}')
