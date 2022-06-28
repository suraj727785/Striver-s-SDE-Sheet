# Question: https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1

def kthElement(arr1, arr2, n, m, k):
    low,high=0,n
    while(low<=high):
        part1=(low+high)//2
        part2=k-part1
        l1=float('-inf') if part1==0 else arr1[part1-1]
        l2=float('-inf') if part2==0 else arr2[part2-1]
        r1=float('inf') if part1==n else arr1[part1]
        r2=float('inf') if part2==m else arr2[part2]
        if l1<=r2 and l2<=r1:
                return arr1[l1] if l1>l2 else arr2[l2]
        if l1>r2:
            high=part1-1
        else:
            low=part1+1
    return 0


arr1=[1,2]
arr2=[3,4]
print(kthElement(arr1,arr2,len(arr1),len(arr2),2))