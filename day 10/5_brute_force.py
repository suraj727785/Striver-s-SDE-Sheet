# Question: https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1#
def findPath(m, n):

    if m[0][0]==0:
        return []
    def solve(m,n,i,j,res,s,V):
        if i==n-1 and j==n-1:
            return True
        if i==n-1 and m[i][j+1]==0:
            return False
        if j==n-1 and m[i+1][j]==0:
            return False
        if i+1<n and j+1<n and m[i][j+1]==0 and m[i+1][j]==0:
            return False
        if i+1<n and m[i+1][j]==1 and [i+1,j] not in V:
            s+='D'
            V.append([i,j])
            if solve(m,n,i+1,j,res,s,V) and s not in res:
                res.append(s)
            s=s[:-1]
            V.pop()
        if j-1>=0 and m[i][j-1]==1 and [i,j-1] not in V:
            s+='L'
            V.append([i,j])
            if solve(m,n,i,j-1,res,s,V):
                res.append(s)
            s=s[:-1]
            V.pop()
        if j+1<n and m[i][j+1]==1 and [i,j+1] not in V:
            s+='R'
            V.append([i,j])
            if solve(m,n,i,j+1,res,s,V):
                res.append(s)
            s=s[:-1]
            V.pop()
        if i-1>=0 and m[i-1][j]==1 and [i-1,j] not in V:
            s+='U'
            V.append([i,j])
            if solve(m,n,i-1,j,res,s,V) and s not in res:
                res.append(s)
            s=s[:-1]
            V.pop()
        
    res=[]
    solve(m,n,0,0,res,'',[])
    return res


m= [[0, 1, 1, 1],
    [1, 1, 1, 0],
    [1, 0, 1, 1],
    [0, 0, 1, 1]]
n=len(m)
print(findPath(m,n))




