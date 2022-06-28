# Question: https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1

def kthElement(arr1, arr2, n, m, k):
    arr1.extend(arr2)
    arr1.sort()
    return arr1[k-1]

nums1=[1,2]
nums2=[3,4]
print(kthElement(nums1,nums2,len(nums1),len(nums2),2))