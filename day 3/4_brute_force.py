# question: https://leetcode.com/problems/majority-element-ii/

def majorityElement(nums):
    dic={}
    res=[]
    for i in range(len(nums)):
        if nums[i] not in dic.keys():
            dic[nums[i]]=1
        else:
            dic[nums[i]]+=1
        if dic[nums[i]]>len(nums)//3:
            if nums[i] not in res:
                res.append(nums[i])
    return res
print(majorityElement([2,2,1,1,1,2,2]))