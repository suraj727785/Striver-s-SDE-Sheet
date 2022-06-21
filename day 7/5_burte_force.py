# question: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(nums):
    li=[]
    i,n=0,len(nums)
    while(i<n):
        if nums[i] in li:
            nums.pop(i)
            n=len(nums)
            i-=1
        else:
            li.append(nums[i])
        i+=1
    return len(nums)
 
nums=[0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
