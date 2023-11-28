#!/usr/bin/env python
# -*-coding:utf-8 -*
import sys
import re

for line in sys.stdin:
    docs = line.lower()
    arr = []
    
    # for char in [",", ".", '"', "'", "(", ")", "\\", ";", ":", "$1", "$", "&"]:
    #     docs = docs.replace(char, '')

    name, docs = docs.split('<splittername>')
    # print(name)
    for word in re.split(r'\W+', docs):
        arr.append('{}\t{}\t{}'.format(word, name, 1))

    for i in sorted(arr):
        print(i)
