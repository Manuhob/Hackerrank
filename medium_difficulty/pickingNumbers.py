#Encontrar la longitud del máximo sub arreglo tal que |a-b| <=1, para todo a,b en el subarreglo.

def pickingNumbers(a):
    a = sorted(a)
    b = sorted(list(set(a)))
    index = 1
    maxim = 1
    for pivot in range(len(a)-1):
        localmax = 1
        for j in range(pivot+1, len(a)):
            if abs(a[j]-a[pivot]) <=1:
                localmax += 1
                if localmax > maxim:
                    maxim = localmax
            else:
                if localmax > maxim:
                    maxim = localmax
                break
    return maxim


a = list(map(int, '12 2 2 1 4 6 7'.split(' ')))

if pickingNumbers(a) == 3:
    print(f'Test case {0}: Success!!')
else:
    print(f'Test case {0}: Failed')
    print(pickingNumbers(a),' vs ',3)

