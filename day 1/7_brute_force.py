def maxProfit(nums):
    p=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if p<nums[j]-nums[i]:
                p=nums[j]-nums[i]
    return p
print(maxProfit([7,1,5,3,6,4]))