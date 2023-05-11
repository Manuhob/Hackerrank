#!/bin/python3
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

import math


def encryption(s):
    # Write your code here
    longword = ''.join(s.strip().split(' '))
    L = len(longword)
    #getting rid of spaces
    floor = math.floor(math.sqrt(L))
    ceil = math.ceil(math.sqrt(L))
    
    
    #Determine 
    rows = ceil
    columns = ceil
    if floor*ceil >= L:
        rows = floor    
    
    grid = []
    for i in range(rows):#filling the grid
        grid.append(longword[i*columns:i*columns + columns])
    resultado = ''

    excedent = L%columns
    
    for i in range(columns):
        for row in grid:
            if i >= len(row):
                continue
            resultado += row[i]
        resultado += ' '
    return resultado.strip()
        

#test string
s = 'wclwfoznbmyycxvaxagjhtexdkwjqhlojykopldsxesbbnezqmixfpujbssrbfhlgubvfhpfliimvmnny'
#Expected output
result = 'wmgjpnull cyjqlejgi lyhhdzbui wctlsqsbm fxeoxmsvv ovxjeirfm zadysxbhn nxkkbffpn bawobphfy'
print('Sucess of program:')
print(encryption(s) == result )

