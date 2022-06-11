def getInversions(arr):
    res=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                res+=1
    return res
print(getInversions([3,1,2,5,3]))