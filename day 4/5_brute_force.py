# question: https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1

def solve(a,b):
    res=0
    for i in range(len(a)):
        xorr=a[i]
        if xorr==b:
            res+=1
        for j in range(i+1,len(a)):
            xorr^=a[j]
            if xorr==b:
                res+=1
    return res


print(solve([4, 2, 2, 6, 4],6))
print((4^2),(4^2))
[4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]
