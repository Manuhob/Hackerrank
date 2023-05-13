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
    # Write your code hee
    return 'thirteen minutes to six'

tests = [(3,00),(5,01),(5,10),(5,15),(5,30),(5,40),(5,45),(5,47),(5,32)]

output_tests = ["three o' clock",'one minute past five', 'ten minutes past five', 'quarter past five', 'half past five', 'twenty minutes to six', 'quarter to six', 'thirteen minutes to six', 'twenty eight minutes past five']

for i in range(3):
    h = tests[i][0]
    m = tests[i][1]
    r = output_tests[i]
    if timeInWords(h,m) == r:
        print(f'Test number {i+1}: Success!!')
    else:
        print(f'Test number {i+1}: Failed!!')


