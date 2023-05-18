def matrixRotation(matrix, r):

    transposed = False
    if len(matrix[0]) < len(matrix):
        matrix = transpose(matrix)
        transposed = True

    strips = matrixtoStrips(matrix)
    
    rotatedstrips = []
    for s in strips:
        rotatedstrips.append(arrayRotation(s,r,transposed))

    result = stripstoMatrix(rotatedstrips)

    if transposed:
        return transpose(result)
    else: return result

def transpose(matrix):
    matriz = []
    for j in range(len(matrix[0])):
        matriz.append([matrix[i][j] for i in range(len(matrix)) ])
    return matriz

def matrixtoStrips(matrix):
    r = len(matrix)
    c = len(matrix[0])
    strips = []
    for j in range(r//2):
        strips.append(matrix[j][j:c-j] + [matrix[i][c-j-1] for i in range(1+j,r-(j+1))] + matrix[r-j-1][j:c-j][::-1] + [matrix[i][j] for i in range(1+j,r-(j+1))][::-1])
    return strips

def arrayRotation(arr, r,boolean):
    if len(arr) < r:
        r = r%len(arr)
    if boolean:
        r = len(arr) - r
        return arr[r:] + arr[:r]
    else: return arr[r:] + arr[:r]


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



#Test case
# r = 2 #power of rotation
# matrix = [[(i + 7*j) for i in range(7)] for j in range(6)]
# rmatrix = [[2, 3, 4, 5, 6, 13, 20], [1, 10, 11, 12, 19, 26, 27], [0, 9, 18, 25, 24, 33, 34], [7, 8, 17, 16, 23, 32, 41], [14, 15, 22, 29, 30, 31, 40], [21, 28, 35, 36, 37, 38, 39]]

matrix = [[1, 2, 3, 4], [7, 8, 9, 10], [13,14,15,16], [19,20,21,22], [25,26,27,28]]
rmatrix = matrixRotation(matrix,7)

print('Original matrix:')
for l in matrix:
    print(' '.join(map(str,l)))

print('\nRotated matrix:')
for l in rmatrix:
    print(' '.join(map(str,l)))
# if matrixRotation(matrix, r) == rmatrix:
#     print(f'Test number {0}: Success!!')
# else:
#     print(f'Test number {0}: Failed!!')
#     print(matrixRotation(matrix, r), ' vs ', rmatrix)
