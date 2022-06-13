# question: https://leetcode.com/problems/majority-element-ii/

def majorityElement(nums):
    nums.sort()
    res=1
    ans=[]
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]:
            res+=1
        else:
            if res>len(nums)//3:
                if nums[i-1] not in ans:
                    ans.append(nums[i-1])
                res=1
            else:
                res=1
    if res>len(nums)//3:
        if nums[-1] not in ans:
            ans.append(nums[-1])
    return ans
print(majorityElement([2,2,1,1,1,2,2]))