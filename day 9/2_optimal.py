# Question: https://leetcode.com/problems/subsets-ii/submissions/


def subsetsWithDup(nums):
    def subset(arr,n,ind,r,res):
        if ind==n:
            if sorted(r[:]) not in res:
                res.append(sorted(r[:]))
            return
        r.append(arr[ind])
        subset(arr,n,ind+1,r,res)
        r.pop()
        subset(arr,n,ind+1,r,res)
    res=[]
    subset(nums,len(nums),0,[],res)
    return res




arr=[1,2,2]
print(subsetsWithDup(arr))
