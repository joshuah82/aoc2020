#!/usr/bin/python3
import sys

MIN_ROW = 0
MAX_ROW = 127
MIN_COL = 0
MAX_COL = 7

with open(f'{sys.path[0]}/day5.txt', 'r') as f:
    seats = [line.strip() for line in f.readlines()]

seat_ids = []
for seat in seats:
    row = -1
    row_lower = MIN_ROW
    row_upper = MAX_ROW

    col = -1
    col_lower = MIN_COL
    col_upper = MAX_COL

    for loc in seat:
        if loc == 'F':
            row_upper = int(((row_upper + row_lower + 1) / 2) - 1)
            row = row_lower
        elif loc == 'B':
            row_lower = int(((row_upper + row_lower + 1) / 2))
            row = row_upper
        elif loc == 'L':
            col_upper = int(((col_upper + col_lower + 1) / 2) - 1)
            col = col_lower
        elif loc == 'R':
            col_lower = int(((col_upper + col_lower + 1) / 2))
            col = col_upper

    seat_id = (row * 8) + col
    seat_ids.append(seat_id)

print(f'Answer: {sorted(seat_ids, reverse=True)[0]}')
