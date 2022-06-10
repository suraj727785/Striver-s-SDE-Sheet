# without using extra space...
def merge(nums1,nums2):
    m,n=len(nums1),len(nums2)
    gap=(m+n)//2
    while(gap>0):
        i=0
        while(i+gap<m+n):
            if i+gap<m:
                if nums1[i]>=nums1[i+gap]:
                    nums1[i],nums1[i+gap]=nums1[i+gap],nums1[i]
            if i<m and i+gap>=m:
                if nums1[i]>=nums2[i+gap-m]:
                    nums1[i],nums2[i+gap-m]=nums2[i+gap-m],nums1[i]
            if i>=m:
                if nums2[i-m]>=nums2[i+gap-m]:
                    nums2[i-m],nums2[i+gap-m]=nums2[i+gap-m],nums2[i-m]
            i+=1
        gap//=2
    return nums1+nums2       
print(merge([1,2,3],[2,5,6])) 