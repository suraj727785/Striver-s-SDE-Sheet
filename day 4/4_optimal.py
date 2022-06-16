# question: https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1

def maxLen(n, arr):
    summ=0
    res=0
    dic={}
    for i in range(n):
        summ+=arr[i]
        if summ==0:
            res=i+1
        elif summ in dic.keys():
            if res<i-dic[summ]:
                res=i-dic[summ]
        else:
            dic[summ]=i
    return res
print(maxLen(8,[15,-2,2,-8,1,7,10,23]))
