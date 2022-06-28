# Question: https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1

def kthElement(arr1, arr2, n, m, k):
    i,j=0,0
    k-=1
    while(i<n and j<m):
        if arr1[i]<arr2[j]:
            if k==0:
                return arr1[i]
            i+=1
        else:
            if k==0:
                return arr2[j]
            j+=1
        k-=1
    while(i<n):
        if k==0:
            return arr1[i]
        i+=1
        k-=1
    while(j<m):
        if k==0:
            return arr2[j]
        j+=1
        k-=1

arr1=[1,2]
arr2=[3,4]
print(kthElement(arr1,arr2,len(arr1),len(arr2),2))