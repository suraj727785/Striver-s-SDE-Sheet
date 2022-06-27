# Question: https://www.interviewbit.com/problems/matrix-median/

def findMedian(a):
    li=[]
    for i in range(len(a)):
        for j in range(len(a[0])):
            li.append(a[i][j])
    li.sort()
    return li[(len(li)//2)+1]
a =[[1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]]
print(findMedian(a))
