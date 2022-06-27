# Question: https://www.interviewbit.com/problems/matrix-median/

def findMedian(a):
    def countSmallerThanEqualToMid(row,mid):
        low,high=0,len(row)-1
        while(low<=high):
            md=(low+high)//2
            if row[md]<=mid:
                low=md+1
            else:
                high=md-1
        return low
    low,high=1,1e9
    while(low<=high):
        mid=(low+high)//2
        count=0
        for i in range(len(a)):
            count+=countSmallerThanEqualToMid(a[i],mid)
        if count<=(len(a)*len(a[0]))//2:
            low=mid+1
        else:
            high=mid-1
    return int(low)

a =[[1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]]
print(findMedian(a))