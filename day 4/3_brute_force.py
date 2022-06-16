# question: https://leetcode.com/problems/longest-consecutive-sequence/

def longestConsecutive(nums):
    nums.sort()
    res=1
    curr=1
    if len(nums)==0:
        return 0
    for i in range(len(nums)-1):
        if nums[i+1]==nums[i]+1:
            curr+=1
        elif nums[i]==nums[i+1]:
            continue
        else:
            if curr>res:
                res=curr
            curr=1
    if curr>res:
        res=curr
    return res
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
