#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#


def nonDivisibleSubset(k, s):
    if k ==1: return 1 #first exception
    res = [x%k for x in s] #array of residues mod k
    recurrence = dict([(x,0) for x in range(k)]) #dict for saving recurrence of residues in array s
    for i in range(len(res)):
        recurrence[res[i]] += 1
    result = 0
    if recurrence[0]>0: result += 1 #Add one multiple of k, if exists

    if k <=3:#Two more special cases
        if k == 2 and recurrence[1]: result += 1
        else: result += max(recurrence[1],recurrence[2])
        return result
    
    for x in range(1,k//2): result += max(recurrence[x],recurrence[k-x])
        
    if k%2 == 0 and recurrence[k/2] > 0: result += 1
    else: result += max(recurrence[k//2],recurrence[k - k//2])

    return result


#Test cases

k = 9
s = '61197933 56459859 319018589 271720536 358582070 849720202 481165658 675266245 541667092 615618805 129027583 755570852 437001718 86763458 791564527 163795318 981341013 516958303 592324531 611671866 157795445 718701842 773810960 72800260 281252802 404319361 757224413 682600363 606641861 986674925 176725535 256166138 827035972 124896145 37969090 136814243 274957936 980688849 293456190 141209943 346065260 550594766 132159011 491368651 3772767 131852400 633124868 148168785 339205816 705527969 551343090 824338597 241776176 286091680 919941899 728704934 37548669 513249437 888944501 239457900 977532594 140391002 260004333 911069927 586821751 113740158 370372870 97014913 28011421 489017248 492953261 73530695 27277034 570013262 81306939 519086053 993680429 599609256 639477062 677313848 950497430 672417749 266140123 601572332 273157042 777834449 123586826'.split(' ')

array = list(map(int, s))

if nonDivisibleSubset(k, array) == 50:
    print(f'Test case {0}: Success!!')
else:
    print(f'Test case {0}: Failed')
    print(nonDivisibleSubset(k, s),' vs ', 50)


