# Question: https://leetcode.com/problems/permutation-sequence/

import math
def getPermutation(n,k,res):
    if len(n)==0:
        return
    r=math.factorial(len(n)-1)
    i=math.ceil(k/r)
    k=k%r
    res.append(n.pop(i-1))
    getPermutation(n,k,res)
n,k=4,9
n=[x for x in range(1,n+1)]
res=[]
getPermutation(n,k,res)
print(res)