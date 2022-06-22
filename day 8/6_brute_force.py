# question: https://www.codingninjas.com/codestudio/problems/1062712?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=1
# same as N meetings in one room

def maximumActivities(start, end):
    li=[]
    res=1
    n=len(start)
    for i in range(n):
        li.append([start[i],end[i]])
    li=sorted(li,key=lambda x:x[1])
    k=li[0][1]
    for i in range(1,len(li)):
        if li[i][0]>=k:
            res+=1
            k=li[i][1]
    return res
start=[1, 6, 2, 4]
end=[2, 7, 5, 8] 
print(maximumActivities(start,end))