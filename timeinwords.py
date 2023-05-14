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

#There's a terrible bug on python3. We cannot add integers as 01, for example,
#0 should not preceed an integer. It is preferable to be treated as a STRING,
#or add the '0' afterwards.

def timeInWords(h, m):

    result = ''

    hours = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten', '11':'eleven','12':'twelve','13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen', '17' : 'seventeen', '18' : 'eighteen', '19': 'nineteen', '20': 'twenty', '21': 'twenty-one', '22': 'twenty-two', '23': 'twenty-three', '0': 'midnight'}

    specialminutes = {'15':'quarter', '30':'half', '0': "o' clock", '1': 'one minute'}

    minutes = {'2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten', '11':'eleven','12':'twelve','13':'thirteen', '14':'fourteen', '16': 'sixteen', '17' : 'seventeen', '18' : 'eighteen', '19': 'nineteen', '20': 'twenty', '21': 'twenty one', '22': 'twenty two', '23': 'twenty three', '24': 'twenty four', '25': 'twenty five', '26': 'twenty six', '27': 'twenty seven', '28': 'twenty eight', '29': 'twenty nine'}

    if str(m) == '0':
        return hours.get(str(h), "midday") + " " + "o' clock"

    if int(m) <= 30:
        if str(m) in specialminutes:
            return specialminutes[str(m)] + " past " + hours.get(str(h), "midday")
        else:
            return minutes[str(m)] + " minutes past " + hours.get(str(h), "midday")  

    M = 60 - int(m)
    H = (int(h) + 1)%12
    if str(M) in specialminutes:
        return specialminutes[str(M)] + " to " + hours.get(str(H), "midday")
    else:
        return minutes[str(M)] + " minutes to " + hours.get(str(H), "midday")  

    return 'thirteen minutes to six'




#########################################
####### Testing function section ########
#########################################


tests = [('10','57'), ('1','1'), ('3','00'),('5','01'),('5','10'),('5','15'),('5','30'),('5','40'),('5','45'),('5','47'),('5','28')]

output_tests = ["three minutes to eleven","one minute past one","three o' clock",'one minute past five', 'ten minutes past five', 'quarter past five', 'half past five', 'twenty minutes to six', 'quarter to six', 'thirteen minutes to six', 'twenty eight minutes past five']

for i in range(len(tests)):
    h = int(tests[i][0])
    m = int(tests[i][1])
    r = output_tests[i]
    if timeInWords(h,m) == r:
        print(f'Test number {i+1}: Success!!')
        print(timeInWords(h,m), '\n')
    else:
        print(f'Test number {i+1}: Failed!!')
        print(timeInWords(h,m), ' vs ', r)
