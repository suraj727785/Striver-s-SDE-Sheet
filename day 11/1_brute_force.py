# Question: https://www.codingninjas.com/codestudio/problems/1062679
def findNthRootOfM(n,m):
    low=1
    high=m
    mid=(low+high)/2
    eps=1e-7
    while(high-low>eps):
        mid=(low+high)/2
        k=pow(mid,n)
        if k<m:
            low=mid
        else:
            high=mid
    mid = str(round(mid, 6))
    mid = str(mid).split('.')
    if len(mid[1])<6:
        mid[1]+='0'*(6-len(mid[1]))     
    mid=mid[0]+'.'+mid[1][:6]
    return mid

print(findNthRootOfM(3,27))
