# question: https://leetcode.com/problems/majority-element/

def majorityElement(nums):
    dic={}
    for i in range(len(nums)):
        if nums[i] not in dic.keys():
            dic[nums[i]]=1
        else:
            dic[nums[i]]+=1
        if dic[nums[i]]>len(nums)//2:
            return nums[i]
print(majorityElement([2,2,1,1,1,2,2]))