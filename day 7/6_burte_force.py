# question: https://leetcode.com/problems/max-consecutive-ones/

def findMaxConsecutiveOnes(nums):
    res=0
    curr=0
    for i in range(len(nums)):
        if nums[i]==1:
            curr+=1
        else:
            if curr>res:
                res=curr
            curr=0
    return res 
nums=[1,0,1,1,0,1]
print(findMaxConsecutiveOnes(nums))
