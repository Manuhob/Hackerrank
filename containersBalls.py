#n containers with n type of balls. We want to sort them in the containers by type, but only with "pairs swapings"

#The following function will tell us if it is possible to do so or not.

#Algorithm description:
    #make a list of amount of balls in each container
    #make a list of amount of balls of each type
    #if after sorting the above lists, we have a coincidence, then return possible, otherwise impossible    
def organizingContainers(container):
    ballsperContainer = [] #amount of balls in each container
    n = len(container[0])
    ballsof_eachtype = [0 for x in range(n)]    #amount of balls of each type
    for inform in container:
        total = 0
        for i in range(n):
            total += inform[i]
            ballsof_eachtype[i] += inform[i]
        ballsperContainer.append(total)
    if sorted(ballsof_eachtype) == sorted(ballsperContainer):
        return 'Possible'
    else:
        return 'Impossible'


if __name__ == '__main__':

    q = 2 #number of queries
    test_cases = [[[1,3,1],[2,1,2],[3,3,3]], [[0,2,1],[1,1,1],[2,0,0]]]
    output =['Impossible', 'Possible']
    for i in range(q):
        if organizingContainers(test_cases[i]) == output[i]:
            print(f'Test case {i+1}: Success!!')
        else:
            print(f'Test case {i+1}: Failed!!')

