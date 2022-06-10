def maxProfit(nums):
    b=nums[0]
    p=0
    for i in range(1,len(nums)):
        if p<nums[i]-b:
            p=nums[i]-b
        if nums[i]<b:
            b=nums[i]
    return p
print(maxProfit([7,1,5,3,6,4]))