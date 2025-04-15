def issafe(matrix,row,col,n):
    for i in range (row):
        if matrix[i][col]==1:
            return False
        
    i,j = row,col
    while i>=0 and j>=0:
        if matrix[i][j]==1:
            return False
        i-=1
        j-=1

    i,j = row,col
    while i>=0 and j<n:
        if matrix[i][j]==1:
            return False
        i-=1
        j+=1
    return True

def printboard(matrix,n):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end='')
        print()
    print()


def nqueen(matrix,n,row):
    if row == n: #base case
        printboard(matrix,n)
        return
    for col in range(n):
        if issafe(matrix,row,col,n):
            matrix[row][col]=1 #place queen
            nqueen(matrix,n,row+1)
            matrix[row][col]=0 #backtrack

n = 3
matrix = [[0]*n for _ in range (n)]
nqueen(matrix,n,0)