#Partial solucion of mine, when len(player) < len(ranked). This is not optimized.
def climbingLeaderboard(ranked, player):
    ranks =sorted(list(set(ranked)), reverse=True) #ranks without repetition.
    resultado = []
    i = 0
    while len(ranks) > 0 and i < len(player):
        onboard = False
        for j in range(len(ranks)):
            if j == 0 and player[i] > ranks[0]:
                resultado.append(1)
                onboard = True
                break
            elif player[i] >= ranks[j] and player[i] < ranks[j-1]:
                ranks = ranks[:j]
                resultado.append(j+1)
                onboard = True
                break
        if not onboard:
            resultado.append(len(ranks)+1)
        i +=1
    return resultado

board = [100, 90, 90, 80, 75, 60]
player = [50, 65, 77, 90, 102]

print(climbingLeaderboard(board,player))



#Optimized solution proposed by Yashwant Parihar at:
#https://thecscience.com/hackerrank-climbing-the-leaderboard-solution.html
def climbingLeaderboard(scores, player):
    scores = list(set(scores))
    scores.sort() #sorted in ascending order, without repetition
    rank = len(scores)+1
    pos = 0
    resultado = []
    for x in player:
        while pos != len(scores) and x >= scores[pos]:
            rank -= 1
            pos += 1
        resultado.append(rank)
    return resultado

print(climbingLeaderboard(board,player))
