# Question: https://leetcode.com/problems/subsets-ii/submissions/


def combinationSum(candidates,ind, target,res,r):
    if target==0:
        if sorted(r[:]) not in res:
            res.append(sorted(r[:]))
        return
    if ind==len(candidates) or target<candidates[ind]:
        return  
    r.append(candidates[ind])
    combinationSum(candidates,ind,target-candidates[ind],res,r)
    r.pop()
    combinationSum(candidates,ind+1,target,res,r)

arr=[2,7,6,3,5,1]
target=9
res=[]
combinationSum(sorted(arr),0,target,res,[])
print(res)
