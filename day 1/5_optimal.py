def sortColors(nums):
    i,j,k,=0,0,len(nums)-1
    while(j<k):
        if nums[j]==2:
            nums[j],nums[k]=nums[k],nums[j]
            k-=1
        if nums[j]==1:
            j+=1
        if nums[j]==0:
            nums[j],nums[i]=nums[i],nums[j]
            i+=1
            j+=1
    if nums[k]==0:
        nums[j],nums[i]=nums[i],nums[j]
    return nums
print(sortColors([2,0,2,1,1,0]))