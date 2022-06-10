# without using extra space...
def merge(nums1,nums2):
    i=0
    while(i<len(nums1)):
        if nums1[i]>nums2[0]:
            nums1[i],nums2[0]=nums2[0],nums1[i]
        i+=1
        for k in range(len(nums2)-1):
            if nums2[k]<=nums2[k+1]:
                break
            nums2[k],nums2[k+1]=nums2[k+1],nums2[k]
    return nums1+nums2
        
print(merge([1,2,3],[2,5,6])) 