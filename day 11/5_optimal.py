# Question: https://leetcode.com/problems/single-element-in-a-sorted-array//

def findMedianSortedArrays(nums1, nums2):
    k=(len(nums1)+len(nums2)-1)//2
    i,j=0,0
    a,b=0
    while(i<len(nums1) and j<len(nums2)):
        k-=1
        if nums1[i]<nums2[j]:
            i+=1
        else:
            j+=1

    if (len(nums1)+len(nums2))%2!=0:
        c=0


nums1=[1,2]
nums2=[3,4]
print(findMedianSortedArrays(nums1,nums2))