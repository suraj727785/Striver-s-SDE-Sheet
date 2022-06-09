def maxSubArray(nums):
    max=float('-inf')
    for i in range(len(nums)):
        sum=0
        for j in range(i,len(nums)):
            sum+=nums[j]
            if sum>max:
                max=sum
    return max
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

