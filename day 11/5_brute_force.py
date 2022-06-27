# Question: https://leetcode.com/problems/single-element-in-a-sorted-array//

def findMedianSortedArrays(nums1, nums2):
    li=[]
    li.extend(nums1)
    li.extend(nums2)
    li.sort()
    if len(li)%2!=0:
        return float(li[len(li)//2])
    return float((li[len(li)//2]+li[(len(li)//2)-1])/2)

nums1=[1,2]
nums2=[3,4]
print(findMedianSortedArrays(nums1,nums2))