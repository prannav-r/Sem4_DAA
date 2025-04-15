def isSafe(matrix,row,col,n): #helper function to check if queen placement is allowed
    for i in range(row):
        if matrix[i][col] == 1: #there is a queen already placed in the column
            return False
    i, j = row, col
    while i >= 0 and j >= 0: #check the diagonal
        if matrix[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i >= 0 and j < n: #check the other diagonal
        if matrix[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True

def printboard(matrix,n):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()
    print()

def nqueen(matrix,n,row):#solving function
    if row==n: #base case
        printboard(matrix,n)
        return
    for col in range(n):
        if(isSafe(matrix,row,col,n)):
            matrix[row][col] = 1#place queen
            nqueen(matrix,n,row+1)#recursive call
            matrix[row][col] = 0#backtrack

n = 4
matrix = [[0] * n for _ in range(n)]  

nqueen(matrix, n, 0)