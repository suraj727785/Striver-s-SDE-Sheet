def sortColors(nums):
    l1=[]
    l2=[]
    l3=[]
    for i in range(len(nums)):
        if nums[i]==0:
            l1.append(0)
        if nums[i]==1:
            l2.append(1)
        if nums[i]==2:
            l3.append(2)
    return l1+l2+l3
print(sortColors([2,0,2,1,1,0]))