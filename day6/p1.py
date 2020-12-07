#!/usr/bin/python3
import sys, re

with open(f'{sys.path[0]}/day6.txt', 'r') as f:
    batch = f.read()

answer = 0
groups = re.split('[\r\n]{2}', batch)
for group in groups:
    questions = []
    people = re.split('[\r\n]', group.strip())
    for idx, person in enumerate(people):
        for question in person:
            questions.append(question)

    questions = sorted(list(dict.fromkeys(questions)))
    answer += len(questions)

print(f'Answer: {answer}')
