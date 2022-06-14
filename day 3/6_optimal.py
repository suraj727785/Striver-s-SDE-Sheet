# question: https://leetcode.com/problems/reverse-pairs/
def reversePairs(nums):
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
        j=m+1
        for i in range(l,m+1):
            while(j<=r and a[i]>2*a[j]):
                j+=1
            c+=(j-(m+1))
        n1=m-l+1
        n2=r-m
        L1,L2=[0]*n1,[0]*n2
        for i in range(n1):
            L1[i]=a[l+i]
        for j in range(n2):
            L2[j]=a[m+1+j]
        # i,j=0,0
        # while(i<n1 and j<n2):
        #     if L1[i]>2*L2[j] and j==n2-1:
        #         c+=j+1
        #         i+=1
        #         j=0
        #     elif L1[i]>2*L2[j]:
        #         j+=1
        #     else:
        #         c+=j
        #         i+=1
        #         j=0
        i,j,k=0,0,l
        while(i<n1 and j<n2):
            if L1[i]<L2[j]:
                a[k]=L1[i]
                i+=1
            else:
                a[k]=L2[j]
                j+=1
            k+=1
        while(i<n1):
            a[k]=L1[i]
            i+=1
            k+=1
        while(j<n2):
            a[k]=L2[j]
            j+=1
            k+=1
        return c
    return mergesort(nums,0,len(nums)-1)    
        
print(reversePairs([40,25,19,12,9,6,2]))
