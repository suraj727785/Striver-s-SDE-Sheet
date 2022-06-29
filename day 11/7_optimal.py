# Question: https://www.interviewbit.com/problems/allocate-books/

def books(a, b):
    low=min(a)
    high=sum(a)
    res=-1
    if len(a)<b:
        return -1
    while(low<=high):
        mid=(low+high)//2
        k=i=r=0
        while(i<len(a)):
            if a[i]>mid:
                k=float('inf')
                break
            if r+a[i]<=mid:
                r+=a[i]
            else:
                r=a[i]
                k+=1
            i+=1
        k+=1
        if k<=b:
            res=mid
            high=mid-1
        else:
            low=mid+1           
    return res
            
a= [ 31, 14, 19, 75 ]
b=12
print(books(a,b))