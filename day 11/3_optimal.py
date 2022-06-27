# Question: https://leetcode.com/problems/single-element-in-a-sorted-array//

# for left half
# even index = 1st instance
# odd index = 2nd instance
# for right half
# odd index = 1st instance
# even index = 2nd instance

def singleNonDuplicate(nums):
    low,high=0,len(nums)-2
    while(low<=high):
        mid=(low+high)//2
        if nums[mid]==nums[mid^1]:
            low=mid+1
        else:
            high=mid-1
    return nums[low]
        
nums = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate(nums))