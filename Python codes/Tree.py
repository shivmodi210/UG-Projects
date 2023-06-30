#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def search(b):
    num = []
    for i in range(m):
        if edges[i][0] == b:
            num.append(edges[i][1])
        else: continue
    return num

def bfs(n, m, edges, s):
    # Write your code here
    arr=[]
    arr = [-1 for i in range(n)]
    
    l = []
    l.append(s)
    while(True):
        i = 1
        for j in range(len(l)):
            num = search(l[j])
            if len(num) == 0: break
            for i in range(len(num)):
                arr[num[i]] = 6*i
        l = num
        i = i + 1
    return arr
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
