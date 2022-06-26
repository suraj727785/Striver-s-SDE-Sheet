# Question: https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1#
def findPath(m, n):

    def solve(m,n,i,j,res,s):
        if i==n-1 and j==n-1:
            return True
        if i==n-1 and m[i][j+1]==0:
            return False
        if j==n-1 and m[i+1][j]==0:
            return False
        if m[i][j+1]==0 and m[i+1][j]==0:
            return -1
        if i+1<n and m[i+1][j]==1:
            s+='D'
            if solve(m,n,i+1,j,res,s):
                res.append(s)
            s=s[:-1]
        if j+1<n and m[i][j+1]==1:
            s+='R'
            if solve(m,n,i,j+1,res,s):
                res.append(s)
            s=s[:-1]
    res=[]
    solve(m,n,0,0,res,'')
    return res


m= [[1, 0, 0, 0],
    [1, 1, 0, 1], 
    [1, 1, 0, 0],
    [0, 1, 1, 1]]
n=len(m)
print(findPath(m,n))




