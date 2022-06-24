# Question: https://leetcode.com/problems/combination-sum-ii/


def combinationSum(candidates,ind, target,res,r):
    if target==0:
        if sorted(r[:]) not in res:
            res.append(sorted(r[:]))
        return 
    for i in range(ind,len(candidates)):
        if i>ind and candidates[i]==candidates[i-1]:
            continue
        if candidates[i]>target:
            break
        r.append(candidates[i])
        combinationSum(candidates,i+1,target-candidates[i],res,r)
        r.pop()

arr=[10,1,2,7,6,1,5]
target=8
res=[]
combinationSum(sorted(arr),0,target,res,[])
print(res)
