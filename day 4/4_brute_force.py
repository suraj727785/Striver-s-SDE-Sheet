# question: https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1

def maxLen(n, arr):
    res=0
    for i in range(n):
        summ=0
        for j in range(i,n):
            summ+=arr[j]
            if summ==0 and res<(j-i+1):
                res=j-i+1
    return res


print(maxLen(8,[15,-2,2,-8,1,7,10,23]))
