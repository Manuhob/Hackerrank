#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    #Algorithm:
    #1. Find biggest i such that w[i] < w[i+1]
    swpind1 = 'Nullindex'
    for i in range(len(w)-1)[::-1]:
        if w[i] < w[i+1]:
            swpind1 = i
            break
    if swpind1 == 'Nullindex':
        return 'no answer'
    #2. Find biggest k such that w[i] < w[i+k]
    swpind2 = swpind1+1
    for i in range(swpind1+1,len(w))[::-1]:
        if w[swpind1] < w[i]:
            swpind2 = i
            break
    #3. swap w[i] with w[i+k] in w,
    s = w[:swpind1]+w[swpind2]+w[swpind1+1:swpind2]+w[swpind1]+w[swpind2+1:]
    #4. sort the word w[i+1:]
    return s[:swpind1+1]+ ''.join(sorted(s[swpind1+1:]))
    

tests = ['dcba', 'dcbb', 'fedcbabcd', 'dkhc']

output_tests = ['no answer', 'no answer', 'fedcbabdc', 'hcdk']

for i in range(4):
    t,r = tests[i], output_tests[i]
    if biggerIsGreater(t) == r:
        print(f'Test number {i+1}: Success!!')
    else:
        print(f'Test number {i+1}: Failed!!')


