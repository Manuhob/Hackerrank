#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    return "three o' clock"

tests = [(5,47), (3,00), (7,15)]

output_tests = ['thirteen minutes to six', "three o' clock", 'quarter past seven']

for i in range(3):
    h = tests[i][0]
    m = tests[i][1]
    r = output_tests[i]
    if timeInWords(h,m) == r:
        print(f'Test number {i+1}: Success!!')
    else:
        print(f'Test number {i+1}: Failed!!')


