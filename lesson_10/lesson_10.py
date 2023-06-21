import time

# f = open('data.txt', mode='r', encoding='utf-8')
# file_data = f.readlines()
"""
file_data = []
line = f.readline()[:-1]
while line != '':
    file_data.append(line)
    line = f.readline()[:-1]

# file_data.append(f.readline())
# file_data.append(f.readline())
# file_data.append(f.readline())
# file_data.append(f.readline())
# file_data.append(f.readline())

print(file_data)
for line in file_data:
    print(line, end='')
"""
# data = f.read()
# print(data)

import os
from datetime import datetime


def add(notes: dict, note: str):
    now = str(datetime.now())
    notes[now] = note

# notes = {}
# add(notes, 'hhjjjj1')
# time.sleep(1)
# add(notes, 'h2hjjjj2')
# time.sleep(1)
# add(notes, 'hdd3')

# out = open('data.txt', mode='a', encoding='utf-8')
# for key in notes:
#     out.write(key + '\n')
#     out.write(notes[key] + '\n')
# out.close()
#
# input_notes = {}
# input = open('data.txt')
# key = input.readline().strip()
# note = input.readline().strip()
# while key:
#     input_notes[key] = note
#     key = input.readline().strip()
#     note = input.readline().strip()
#
# print(input_notes)

def file_write_method(notes: dict):
    out = open('data.txt', mode='w', encoding='utf-8')
    for key in notes:
        out.write(key + '\n')
        out.write(notes[key] + '\n')
    out.close()


def input_notes():
    input_notes = {}
    input = open('data.txt', mode='r', encoding='utf-8')
    key = input.readline().strip()
    note = input.readline().strip()
    while key:
        input_notes[key] = note
        key = input.readline().strip()
        note = input.readline().strip()
    return input_notes

if __name__ == '__main__':
    # f = open('data.txt', mode='r', encoding='utf-8')

    a = input_notes()
    print(a)


