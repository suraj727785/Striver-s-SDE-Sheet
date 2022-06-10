def merge(nums1, m, nums2, n):
    for i in range(m,m+n):
        nums1[i]=nums2[i-m]
    nums1.sort()
    return nums1
print(merge([1,2,3,0,0,0],3,[2,5,6],3))