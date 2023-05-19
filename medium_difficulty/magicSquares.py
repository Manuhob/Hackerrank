# Computing the minimal cost of transforming a given matrix into a magic square

def rotating_matrix(m):
    rotated = []
    for i in range(3):
        rotated.append([m[j][2-i] for j in range(3)])
    return rotated


def reflecting_matrix(m):
    reflected = []
    for i in range(3):
        reflected.append([m[j][i] for j in range(3)])
    return reflected

sq = [[4,9,2],[3,5,7],[8,1,6]]
magic_squares=[]
for _ in range(2):
    for _ in range(4):
        magic_squares.append(sq)
        sq = rotating_matrix(sq)
    sq = reflecting_matrix(sq)

def transformation_cost(a,b):
    cost = 0
    for i in range(3):
        for j in range(3):
            cost += abs(a[i][j] - b[i][j])
    return cost
    
def formingMagicSquare(s):
    # Write your code here
    minimumcost = 100
    for i in range(8):
        if minimumcost > transformation_cost(s,magic_squares[i]):
            minimumcost = transformation_cost(s,magic_squares[i])
    return minimumcost

s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]


if formingMagicSquare(s) == 7:
    print(f'Test case {0}: Success!!')
else:
    print(f'Test case {0}: Failed')
    print(formingMagicSquare(s) ,' vs ', 7)

