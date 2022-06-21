# question: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(nums):
    if len(nums)==0:
        return nums
    last=nums[0]
    i,n=1,len(nums)
    while(i<n):
        if nums[i]==last:
            nums.pop(i)
            n=len(nums)
        else:
            last=nums[i]
            i+=1
    return nums
 
nums=[0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
