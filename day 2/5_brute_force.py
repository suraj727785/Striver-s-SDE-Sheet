def repeatedNumber(a):
        b=[0]*(len(a)+1)
        c=[0]*2
        for i in range(len(a)):
            b[a[i]]+=1
        for i in range(1,len(b)):
            if(b[i]==2):
                c[0]=i
            if(b[i]==0):
                c[1]=i
        return c
print(repeatedNumber([3,1,2,5,3]))