def findDuplicate(nums):
    li=[0]*(len(nums))
    for i in range(len(nums)):
        if li[nums[i]]==0:
            li[nums[i]]+=1
        else:
            return nums[i]
print(findDuplicate([1,3,4,2,2]))