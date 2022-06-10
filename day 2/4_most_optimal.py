def findDuplicate(nums):
    s,f=nums[0],nums[0]
    s=nums[s]
    f=nums[nums[f]]
    while(s!=f):
        s=nums[s]
        f=nums[nums[f]]
    f=nums[0]
    while(s!=f):
        s=nums[s]
        f=nums[f]
    return s
print(findDuplicate([1,3,4,2,2]))