# Question: https://practice.geeksforgeeks.org/problems/subset-sums2234/1
# used power set

def subsetSums(arr, n):
    res=[]
    l=len(bin(pow(2,n)-1)[2:])
    for i in range(pow(2,n)):
        t=[int(x) for x in bin(i)[2:]]
        k=[0]*(l-len(t))+t
        res.append(sum([arr[i]*k[i] for i in range(len(arr))]))
    
    return sorted(res)

a=[1,2,5]
print(subsetSums(a,len(a)))