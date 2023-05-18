

def matrixRotation(matrix, r):
    print('matriz original:')
    for l in matrix:
        print(' '.join(map(str, l)))

    transpose = False
    if len(matrix[0]) < len(matrix):
        matrix = transpose(matrix)
        transpose = True
    strips = matrixtoStrips(matrix)
    
    print('printing strips')
    for s in strips:
        print(s)
    #rotar bandas 'arrayRotation'
    rotatedstrips = []
    for s in strips:
        rotatedstrips.append(arrayRotation(s,r))

    print('printing rotated strips')
    for s in rotatedstrips:
        print(s)
    #insertar bandas de nuevo en la matriz
    result = stripstoMatrix(rotatedstrips)

    print('rotated matrix')
    for l in result:
        print(' '.join(map(str, l)))

    if transpose:
        return transpose(result)
    else: return result

def transpose(matrix):
    matriz = []
    for j in range(len(matrix[0])):
        matriz.append([matrix[i][j] for i in range(len(matrix)) ])
    return matriz

def matrixtoStrips(matrix):
    #under supposition that rows <= columns and rows%2 == 0.
    r = len(matrix)
    c = len(matrix[0])
    strips = []
    for j in range(r//2):
        strips.append(matrix[j][j:c-j] + [matrix[i][c-j-1] for i in range(1+j,r-(j+1))] + matrix[r-j-1][j:c-j][::-1] + [matrix[i][j] for i in range(1+j,r-(j+1))][::-1])
    return strips

def arrayRotation(arr, r):
    if len(arr) < r:
        r = r%len(arr)
    return arr[r:] + arr[:r]


def consiguiendo(array):
    r = 2*len(array)
    c = len(array[0])//2 + 2 - r
    matrix = [[0 for _ in range(c)] for _ in range(r)]
    strip = array[0]
    strip1 = strip[0:c]
    strip2 = strip[c:c+r-2]
    strip3 = strip[c+r-2:2*c+r-2][::-1]
    strip4 = strip[2*c+r-2:][::-1] 

    for i in range(c):
        matrix[0][i] = strip1[i]
        matrix[r-1][i] = strip3[i]
    for i in range(1,r-1):
        matrix[i][c-1] = strip2[i-1]
        matrix[i][0] = strip4[i-1]
    return matrix

#La anterior ya puso la cinta exterior, vamos a modificarla:
def stripstoMatrix(array):
    r = 2*len(array)
    c = len(array[0])//2 + 2 - r
    matrix = [[0 for _ in range(c)] for _ in range(r)]
#    j = 2
    for j in range(len(array)):
        strip = array[j]
        strip1 = strip[0:c-2*j]
        strip2 = strip[c-2*j:c+r-2*(2*j + 1)]
        strip3 = strip[c+r-2*(2*j + 1):2*c+r-2*(3*j + 1)][::-1]
        strip4 = strip[2*c+r-2*(3*j + 1):][::-1] 

        for i in range(j,c-j):
            matrix[j][i] = strip1[i-j]
            matrix[r-(j+1)][i] = strip3[i-j]
        for i in range(j+1,r-(j+1)):
            matrix[i][c-(j+1)] = strip2[i-(j+1)]
            matrix[i][j] = strip4[i-(j+1)]
    return matrix




#Test case creation
def stringtoarray(s):
    result = []
    for x in s:
        result.append(x)
    return result

tests = []


r = 2 #power of rotation
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

#testing matrixtoStrips with large matrix 
#matrix = []
#for j in range(6):
#    matrix.append([(i + j*7)  for i in range(7)])

#rows and columns
r=len(matrix)
c=len(matrix[0])

#Test case 2
rmatrix = [[3,4,8,12], [2,11,10,16], [1,7,6,15],[5,9,13,14]]

print('Original matrix:')
for l in matrix:
    print(' '.join(map(str, l)))

print(' ')

#print('The strips and their rotations of the matrix are:')
#strp = matrixtoStrips(matrix)
#for s in strp:
#    print(' '.join(map(str, s)))
#    print(' '.join(map(str, arrayRotation(s,3))), '\n')

print(f'We are rotating {r}-times')
matrixRotation(matrix,r)

#if matrixRotation(matrix, r) == rmatrix:
#    print(f'Test number {0}: Success!!')
#    print(matrixRotation(matrix, r), '\n')
#else:
#    print(f'Test number {0}: Failed!!')
#    print(matrixRotation(matrix, r), ' vs ', rmatrix)
