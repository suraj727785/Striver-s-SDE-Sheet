# Question: https://leetcode.com/problems/permutations/

def permute(nums,ind,res):
        if ind==len(nums):
            res.append(nums[:])
            return
        for i in range(ind,len(nums)):
            nums[i],nums[ind]=nums[ind],nums[i]
            permute(nums,ind+1,res)
            nums[i],nums[ind]=nums[ind],nums[i]

nums=[1,2,3]
res=[]
permute(nums,0,res)
print(res)