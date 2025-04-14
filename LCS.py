#dp table

def lcs(str1,str2):
    x=len(str1)
    y=len(str2)
    dp=[[0 for _ in range(y+1)] for _ in range(x+1)]

    for i in range(1,x+1):
        for j in range(1,y+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])

    ans=[]
    i,j=x,y
    while i>0 and j>0:
        if str1[i-1]==str2[j-1]:
            ans.insert(0,str1[i-1])
            i-=1
            j-=1

        elif dp[i-1][j]>dp[i][j-1]:
                i-=1
        else:
                j-=1

    return ans

print(lcs("ABCB","BDC"))