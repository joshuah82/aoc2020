#!/usr/bin/python3
import sys

TARGET = 2020

with open(f'{sys.path[0]}/day1.txt', 'r') as f:
    nums = [int(num.strip()) for num in f.readlines()]

for x in range(len(nums)):
    num1 = nums[x]
    for num2 in nums[x+1:]:
        for num3 in nums[x+2:]:
            if (num1 + num2 + num3) == TARGET:
                print(f'Found:  {num1} + {num2} + {num3} = {TARGET}')
                print(f'Answer: {num1} * {num2} * {num3} = {num1 * num2 * num3}')
                exit()
