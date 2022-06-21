# question: https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1

def maximumMeetings(n,start,end):
    li=[]
    res=[1]
    for i in range(n):
        li.append([start[i],end[i],i])
    sorted(li,key=lambda x:x[1])
    print(li)
    k=li[0][1]
    for i in range(1,len(li)):
        if li[i][0]>k:
            res.append(li[i][2]+1)
            k=li[i][0]
    return res

start = [1,3,0,5,8,5]
end =  [2,4,6,7,9,9]
print(maximumMeetings(len(start),start,end))
