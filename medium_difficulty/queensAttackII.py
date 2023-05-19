# Queen's Attack II:
#You will be given a square chess board with one queen and a number of obstacles placed on it. Determine how many squares the queen can attack. 
def queensAttack(n, k, r_q, c_q, obstacles):
    #Amount of squares accesible by queen (without obstacles):
    right= n - c_q
    left = c_q - 1
    up = n - r_q
    down = r_q -1
    left_down = min(r_q, c_q) - 1
    right_up = n - abs(r_q - c_q) - min(r_q, c_q)
    left_up = min(n - r_q, c_q - 1)
    right_down = min(n - c_q, r_q -1)
    
    #reducing the possibilities
    for obst in obstacles:
        r,c = obst[0], obst[1]
        #restricting horizontal moves
        if r == r_q:
            if c < c_q and c_q - c - 1 < left:
                left = c_q - c - 1
            elif c > c_q and c - c_q - 1 < right:
                right = c - c_q - 1
        #restricting vertical moves
        if c == c_q:
            if r < r_q and r_q - r - 1 < down:
                down = r_q - r - 1
            elif r > r_q and r - r_q - 1 < up:
                up = r - r_q - 1
        #restricting diagonal moves
        if (r_q - c_q) == (r-c):
            if c < c_q and (min(r_q, c_q) - min(r,c)-1) < left_down:
                left_down = min(r_q, c_q) - min(r,c) - 1
            elif c > c_q and (min(r,c) - min(r_q,c_q) - 1) < right_up:
                right_up = min(r,c) - min(r_q,c_q) - 1
        #restricting antidiagonal moves 
        if (r_q + c_q) == (r + c):
            if c < c_q and (min(n - r_q, c_q - 1) - min(n - r, c - 1) - 1) < left_up:
                left_up = min(n - r_q, c_q - 1) - min(n - r, c - 1) - 1
            elif c > c_q and (min(n - r, c - 1) - min(n - r_q, c_q - 1) - 1) < right_down:
                right_down = min(n - r, c - 1) - min(n - r_q, c_q - 1) - 1

    horizontal = right + left
    vertical = up + down
    first_diagonal = right_up + left_down
    second_diagonal = right_down + left_up
    result = horizontal + vertical + first_diagonal + second_diagonal
    return result


#Test case
n = 88587 #board dimensions
k = 9 #Number of obstacles
#Queen possition
r_q = 20001 
c_q = 20003

obstacles = [[20001, 20002], [20001, 20004], [20000, 20003], [20002, 20003], [20000, 20004], [20000, 20002], [20002, 20004], [20002, 20002], [564, 323]]

if queensAttack(n,k,r_q,c_q,obstacles) == 0:
    print(f'Test case {0}: Success!!')
else:
    print(f'Test case {0}: Failed')
    print(queensAttack(n,k,r_q,c_q,obstacles), ' vs ',0)


# dimensions = list(map(int, input().rstrip().split()))
# queenposition = list(map(int, input().rstrip().split()))
# obstacles = []
# for _ in range(dimensions[1]):
#     obstacles.append(list(map(int, input().rstrip().split())))
# queensAttack(dimensions[0], dimensions[1], queenposition[0], queenposition[0], obstacles)
#
#Test values
# 100000 0
#4187 5068
