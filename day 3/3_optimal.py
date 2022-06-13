# question: https://leetcode.com/problems/majority-element/
# algo used: moore voting
def majorityElement(nums):
    count=0
    el=0
    for i in range(len(nums)):
        if count==0:
            el=nums[i]
        if el==nums[i]:
            count+=1
        else:
            count-=1
    return el
    
print(majorityElement([2,2,1,1,1,2,2]))