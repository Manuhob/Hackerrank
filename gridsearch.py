#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    C = len(G[0])
    c = len(P[0])
    R = len(G)
    r = len(P)
    if C < c :
        return 'NO'

    for j in range(len(G)):
        if r > R - j:
            return 'NO'
        for i in range(C - c + 1):
            if arrayComparison(G,P,j,i) == 'YES':
                return 'YES'
    return 'NO'

def arrayComparison(G,P,j,i):
    for k in range(len(P)):
        if ''.join(P[k]) != ''.join(G[j+k][i:i+len(P[k])]):
            return 'NO'
    return 'YES'


#Test case creation
def stringtoarray(s):
    result = []
    for x in s:
        result.append(x)
    return result

tests = []

#Test case 2
s = '7283455864 6731158619 8988242643 3830589324 2229505813 5633845374 6473530293 7053106601 0834282956 4607924137'
G = []
for x in s.split(' '):
    G.append(stringtoarray(x))
s = '9505 3845 3530'
P = []
for x in s.split(' '):
    P.append(stringtoarray(x))
tests.append((G,P))

#Test case 2
s = '400453592126560 114213133098692 474386082879648 522356951189169 887109450487496 252802633388782 502771484966748 075975207693780 511799789562806 404007454272504 549043809916080 962410809534811 445893523733475 768705303214174 650629270887160'
G = []
for x in s.split(' '):
    G.append(stringtoarray(x))
s = '99 99'
P = []
for x in s.split(' '):
    P.append(stringtoarray(x))

tests.append((G,P))

output_tests = ['YES', 'NO']



#Testing cases with function
for i in range(len(tests)):
    G = tests[i][0]
    P = tests[i][1]
    r = output_tests[i]
    if gridSearch(G,P) == r:
        print(f'Test number {i+1}: Success!!')
        print(gridSearch(G,P), '\n')
    else:
        print(f'Test number {i+1}: Failed!!')
        print(gridSearch(G,P), ' vs ', r)

















