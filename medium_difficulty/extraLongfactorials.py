#Lo hacemos de manera iterativa, no recursiva por si excedemos el limite de recursion que en python probablemente
#sea 1000
def extraLongFactorials(n):
    if n <= 1: print('1')
    else:
        j,facto = 1,1
        while j <= n:
            facto *= j
            j += 1
        print(facto)
n=int(input('Factorial of: '))
extraLongFactorials(n)
