# question: https://leetcode.com/problems/unique-paths/

def uniquePaths(m,n):
    def solve(m,n,i,j,dp):
        if i==m-1 and j==n-1:
            return 1
        if i>=m or j>=n:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        else:
            dp[i][j]=solve(m,n,i+1,j,dp) + solve(m,n,i,j+1,dp)
            return dp[i][j]
    return solve(m,n,0,0,[[-1]*(n+1)]*(m+1))

print(uniquePaths(3,7))