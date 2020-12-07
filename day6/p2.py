#!/usr/bin/python3
import sys, re

with open(f'{sys.path[0]}/day6.txt', 'r') as f:
    batch = f.read()

answer = 0
groups = re.split('[\r\n]{2}', batch)
for group in groups:
    questions = {}
    people = re.split('[\r\n]', group.strip())
    people_count = len(people)
    for idx, person in enumerate(people):
        for question in person:
            if question not in questions.keys():
                questions[question] = []
            questions[question].append(idx)

    for question in questions:
        if len(questions[question]) == people_count:
            answer += 1

print(f'Answer: {answer}')
