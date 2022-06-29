# Question: https://www.interviewbit.com/problems/allocate-books/

def books(a, b):
    low=min(a)
    high=sum(a)
    while(low<=high):
        mid=(low+high)//2
        k=i=r=0
        res=float('inf')
        maxx=0
        while(i<len(a)):
            if r+a[i]<=mid:
                r+=a[i]
            else:
                if maxx<r:
                    maxx=r
                r=a[i]
                k+=1
            i+=1
            print(r,mid,maxx)
            if res>maxx:
                res=maxx
        if k>b:
            low=mid+1
        else:
            high=mid-1
    return res
            
a=[12, 34, 67, 90]
b=2
print(books(a,b))