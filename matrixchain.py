import math

def matrix_chain_multiplication(dim):
    n = len(dim) - 1
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    C = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for d in range(1, n):
        for i in range(1, n - d + 1):
            j = i + d
            min_cost = math.inf
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + dim[i-1]*dim[k]*dim[j]
                if cost < min_cost:
                    min_cost = cost
                    C[i][j] = k
            dp[i][j] = min_cost

    
    

    

    return dp[1][n]


x = [2, 1, 3, 4, 1]
print(matrix_chain_multiplication(x))