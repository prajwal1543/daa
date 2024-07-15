import math
import os
import random
import re
import sys
sys.setrecursionlimit(10**6)

# Complete the 'unboundedKnapsack' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr

def Knapsack(n, k, arr, memo):
    if k == 0 or n == 0:
        return 0
    if memo[n][k] != 0:
        return memo[n][k]
        
    if arr[n-1] <= k:
        memo[n][k] = max(arr[n-1] + Knapsack(n, k - arr[n-1], arr, memo),
                         Knapsack(n - 1, k, arr, memo))
    else:
        memo[n][k] = Knapsack(n - 1, k, arr, memo)
    
    return memo[n][k]

def unboundedKnapsack(k, arr):
    n = len(arr)
    memo = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    return Knapsack(n, k, arr, memo)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    t = int(input().strip())
    for _ in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        arr = list(map(int, input().rstrip().split()))
        result = unboundedKnapsack(k, arr)
        fptr.write(str(result) + '\n')
    
    fptr.close()
