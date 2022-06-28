# Question: https://leetcode.com/problems/single-element-in-a-sorted-array//

def findMedianSortedArrays(nums1, nums2):
    n1,n2=len(nums1),len(nums2)
    low,high=0,n1
    while(low<=high):
        part1=(low+high)//2
        part2=(n1+n2+1)//2-part1
        l1=float('-inf') if part1==0 else nums1[part1-1]
        l2=float('-inf') if part2==0 else nums2[part2-1]
        r1=float('inf') if part1==n1 else nums1[part1]
        r2=float('inf') if part2==n2 else nums2[part2]
        if l1<=r2 and l2<=r1:
            if (n1+n2)%2==0:
                return (max(l1,l2)+min(r1,r2))/2
            else:
                return max(l1,l2)
        if l1>r2:
            high=part1-1
        else:
            low=part1+1
    return 0


nums1=[1,2]
nums2=[3,4]
print(findMedianSortedArrays(nums1,nums2))