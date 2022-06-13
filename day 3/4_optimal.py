# question: https://leetcode.com/problems/majority-element-ii/
# algo used: moore voting
def majorityElement(nums):
    count1,count2=0,0
    el1,el2=-1,-1
    for i in range(len(nums)):
        if el1==nums[i]:
            count1+=1
        elif el2==nums[i]:
            count2+=1
        elif count1==0:
            el1=nums[i]
            count1=1
        elif count2==0:
            el2=nums[i]
            count2=1
        else:
            count1-=1
            count2-=1
    if nums.count(el1)<=len(nums)//3 and nums.count(el2)<=len(nums)//3:
        return []
    if nums.count(el1)<=len(nums)//3 or el1==el2:
        return [el2]
    if nums.count(el2)<=len(nums)//3:
        return [el1]
    return [el2,el1]
    
print(majorityElement([1,2,3]))