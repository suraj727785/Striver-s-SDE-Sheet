# Question: https://leetcode.com/problems/single-element-in-a-sorted-array//

def singleNonDuplicate(nums):
    i=1
    while i<len(nums):
        if nums[i]==nums[i-1]:
            i+=2
        else:
            break
    return nums[i-1]

nums = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate(nums))