#!/usr/bin/python3
import sys

TARGET = 2020

with open(f'{sys.path[0]}/p1.txt', 'r') as f:
    nums = [int(num.strip()) for num in f.readlines()]

for x in range(len(nums)):
    num1 = nums[x]
    for num2 in nums[x+1:]:
        if (num1 + num2) == TARGET:
            print(f'Found:  {num1} + {num2} = {TARGET}')
            print(f'Answer: {num1} * {num2} = {num1 * num2}')
            exit()
