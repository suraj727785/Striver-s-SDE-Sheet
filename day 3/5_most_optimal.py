# question: https://leetcode.com/problems/unique-paths/

def uniquePaths(m,n):
    ans=1
    for i in range(m+n-2,n-1,-1):
        ans*=i
    for i in range(1,m):
        ans//=i
    return ans

print(uniquePaths(3,7))