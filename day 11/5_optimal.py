# Question: https://leetcode.com/problems/single-element-in-a-sorted-array//

def findMedianSortedArrays(nums1, nums2):
    k=((len(nums1)+len(nums2)-1)//2)
    i,j=0,0
    a=[]
    while(i<len(nums1) and j<len(nums2)):
        if nums1[i]<nums2[j]:
            if len(a)==2:
                break
            if k<=0:
                a.append(nums1[i])
            i+=1
        else:
            if len(a)==2:
                break
            if k<=0:
                a.append(nums2[j])
            j+=1
        k-=1
    while(i<len(nums1)):
        if len(a)==2:
            break
        if k<=0:
            a.append(nums2[i])
        i+=1
        k-=1
    while(j<len(nums2)):
        if len(a)==2:
            break
        if k<=0:
            a.append(nums2[j])
        j+=1
        k-=1
    if (len(nums1)+len(nums2))%2!=0:
        return float(a[0])
    return (a[0]+a[1])/2


nums1=[1,2]
nums2=[3,4]
print(findMedianSortedArrays(nums1,nums2))