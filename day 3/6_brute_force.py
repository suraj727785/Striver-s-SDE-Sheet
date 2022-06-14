# question: https://leetcode.com/problems/reverse-pairs/

def reversePairs(nums):
    c=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]>2*nums[j]:
                c+=1
    return c
print(reversePairs([2,4,3,5,1]))
