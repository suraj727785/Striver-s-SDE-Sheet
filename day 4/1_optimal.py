# question : https://leetcode.com/problems/two-sum/
def twoSum(nums,target):
    dic={}
    for i in range(len(nums)):
        if target-nums[i] in dic.values():
            return [list(dic.keys())[list(dic.values()).index(target-nums[i])],i]
        else:
            dic[i]=nums[i]
print(twoSum([2,7,11,15],9))