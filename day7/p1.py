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

valid_containers = []
def find_containers(contents, containers):
    for container in containers:
        if container not in valid_containers and contents in containers[container].keys():
            valid_containers.append(container)

find_containers(MY_BAG, rules)
for container in valid_containers:
    find_containers(container, rules)

print(f'Answer: {len(valid_containers)}')
