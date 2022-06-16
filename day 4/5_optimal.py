# question: https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1

def solve(a,b):
    res=0
    dic={}
    xorr=0
    for i in range(len(a)):
        xorr^=a[i]
        if xorr^b in dic:
            res+=dic[xorr^b]
        if xorr==b:
            res+=1
        if xorr in dic:
            dic[xorr]+=1
        else:
            dic[xorr]=1
    return res
print(solve([4, 2, 2, 6, 4],6))

