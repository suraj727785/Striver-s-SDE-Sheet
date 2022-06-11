def repeatedNumber(a):
        n=len(a)
        r=a[0]
        for i in range(1,n):
            r=r^a[i]
        s=1
        for i in range(2,n+1):
            s=s^i
        b=s^r
        t=len(bin(b)[2:])
        b1=0
        bb1=[]
        b2=0
        for x in a:
            if x & (1 << (t - 1)):
                bb1.append(x)
                b1=b1^x
            else:
                b2=b2^x
        for i in range(1,n+1):
            if i & (1 << (t - 1)):
                b1=b1^i
            else:
                b2=b2^i
        if b1 in bb1:
            return [b1,b2]
        return [b2,b1]
print(repeatedNumber([3,1,2,5,3]))