# question: https://leetcode.com/problems/powx-n/

def myPow(x,n):
        ans=1
        k=False
        if n<0:
            k=True
            n=-1*(n)
        while(n!=0):
            if n%2:
                ans*=x
                n-=1
            else:
                x*=x
                n//=2
        if k:
            ans=1/ans
        return ans
print(myPow(2.00000,10))