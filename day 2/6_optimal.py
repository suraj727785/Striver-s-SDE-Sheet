def getInversions(arr):
    def mergesort(a,l,r):
        c=0
        if l<r:
            m=l+(r-l)//2
            c+=mergesort(a,l,m)
            c+=mergesort(a,m+1,r)
            c+=merge(a,l,m,r)
        return c
        
    def merge(a,l,m,r):
        c=0
        n1=m-l+1
        n2=r-m
        L,R=[0]*n1,[0]*n2
        for i in range(n1):
            L[i]=a[l+i]
        for i in range(n2):
            R[i]=a[m+1+i]
        i,j,k=0,0,l 
        while(i<n1 and j<n2):
            if L[i]<R[j]:
                a[k]=L[i]
                i+=1
            else:
                c+=len(L)-i
                a[k]=R[j]
                j+=1
            k+=1
        while(i<n1):
            a[k]=L[i]
            i+=1
            k+=1
        while(j<n2):
            a[k]=R[j]
            j+=1
            k+=1
        return c
    return mergesort(arr,0,len(arr)-1)

a=[5,3,2,4,1]
print(getInversions(a))