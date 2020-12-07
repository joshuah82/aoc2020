#!/usr/bin/python3
import sys, re

MY_BAG = 'shiny gold'

with open(f'{sys.path[0]}/day7.txt', 'r') as f:
    rule_list = [line.strip() for line in f.readlines()]

rules = {}
for rule in rule_list:
    container_type, contents = re.split(' bags contain ', rule)

    if container_type not in rules.keys():
        rules[container_type] = {}

    if contents != 'no other bags.':
        for bags in re.split(', ', re.sub(' bags?\.?', '', contents)):
            bag_count, bag_type = re.search('(\d+) (.+)', bags).groups()
            rules[container_type][bag_type] = bag_count

total_bags = 0
def count_contents(container):
    count = 0
    for bag in rules[container]:
        num_bags = int(rules[container][bag])
        count += num_bags
        count += num_bags * count_contents(bag)

    return count

total_bags += count_contents(MY_BAG)

print(f'Answer: {total_bags}')
