#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
  
# Initializing a queue
#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

class Nodo:
    def __init__(self,data):
        self.data = data
        self.level = -1
        self.left = None
        self.right = None


def swapNodes(indexes, queries):
    # Write your code here
    t = Tree(indexes)
    result = []
    for k in queries:
        q = deque([t])
        node = q.popleft()

        while node:
            if node.level%k == 0:
                node = singleSwap(node)
            for sig in [node.left, node.right]:
                if sig != None:
                    q.append(sig)
            if len(q) > 0:
                node = q.popleft()
            else:
                node = None
        result.append(inOrder(t))

    return result

def singleSwap(root):
    izq = root.left
    root.left = root.right
    root.right = izq

    return root


def inOrder(root):
    if root == None:
        return []
    else:
        return inOrder(root.left) + [root.data] + inOrder(root.right)

def Tree(indexes):
    root = Nodo(1)
    root.level = 1
    q = deque([root])

    for indexpair in indexes:
        current_node = q.popleft()
        lev = current_node.level
        if indexpair[0] != -1:
            newNode = Nodo(indexpair[0])
            newNode.level = lev + 1
            current_node.left = newNode
            q.append(newNode)

        if indexpair[1] != -1:
            newNode = Nodo(indexpair[1])
            newNode.level = lev + 1
            current_node.right = newNode
            q.append(newNode)
    "Podemos regresar la profundidad del árbol en caso que necesitemos optimizar el programa"
    return root

if __name__ == '__main__':
    "Working test case"
    indexes = [[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], [-1, -1], [10, 11],
[-1, -1], [-1, -1], [-1, -1]]

    queries = [2,4]

    result = swapNodes(indexes, queries)

    print(f'indexes: \n {indexes} \n')

    print(f'queries: \n {queries} \n')

    print('Expected output \n2 9 6 4 1 3 7 5 11 8 10 \n2 6 9 4 1 3 7 5 10 8 11')
    
    t = Tree(indexes)
    print('Original tree')
    print(' '.join(map(str,inOrder(t))))

    print('After the first swap')
    print('\n'.join([ ' '.join(map(str, x)) for x in result]))



# A beautiful solution based on an inOrder swapping!

# sys.setrecursionlimit(int(1e9))
#
# def swapNodes(t, queries):
#     t = [[]] + t  # make 1-based indexes work
#     def f(k,r=1,d=1):
#         t[r] = t[r] if d%k else t[r][::-1]
#         return f(k,t[r][0],d+1)+[r]+f(k,t[r][1],d+1) if r+1 else []
#     return [f(i) for i in queries]
