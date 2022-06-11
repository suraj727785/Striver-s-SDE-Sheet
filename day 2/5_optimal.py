# sum of n numbers=n(n+1)/2
# sum of square of n numbers=n(n+1)(2n+1)/6
def repeatedNumber(a):
        c=[0]*2
        n=len(a)
        s=(n*(n+1))//2-sum(a)
        ss=(n*(n+1)*(2*n+1))//6-sum([x*x for x in a])
        a=ss//s
        c[0]=(a+s)//2
        c[1]=c[0]-s
        return c
print(repeatedNumber([3,1,2,5,3]))