def maxSubArray(nums):
    max=float('-inf')
    summ=0
    for i in range(len(nums)):
        summ+=nums[i]
        if max<summ:
            max=summ
        if summ<=0:
            summ=0     
    return max
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

