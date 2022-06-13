# question: https://leetcode.com/problems/unique-paths/

def uniquePaths(m,n):
    def solve(m,n,i,j):
        if i==m-1 and j==n-1:
            return 1
        if i>=m or j>=n:
            return 0
        else:
            return solve(m,n,i+1,j) + solve(m,n,i,j+1)
    return solve(m,n,0,0)

print(uniquePaths(3,7))