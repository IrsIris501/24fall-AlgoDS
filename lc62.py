def uniquepaths(m, n):
    dp=[[0 for i in range(m+1)] for j in range(n+1)]
    dp[0][1]=1
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    return dp[n][m]

m, n=map(int, input().split())
print(uniquepaths(m, n))
