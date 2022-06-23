# Question: https://practice.geeksforgeeks.org/problems/subset-sums2234/1


def subsetSums(arr,n,ind,summ,res):
    if ind==n:
        res.append(summ)
        summ=0
        return
    subsetSums(arr,n,ind+1,summ+arr[ind],res)
    subsetSums(arr,n,ind+1,summ,res)
arr=[1,2,5]
res=[]
subsetSums(arr,len(arr),0,0,res)
print(sorted(res))
