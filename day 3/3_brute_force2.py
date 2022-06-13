# question: https://leetcode.com/problems/majority-element/

def majorityElement(nums):
    nums.sort()
    res=1
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]:
            res+=1
        else:
            if res>len(nums)//2:
                return nums[i-1]
            else:
                res=1
    if res>len(nums)//2:
            return nums[-1]
    
print(majorityElement([2,2,1,1,1,2,2]))