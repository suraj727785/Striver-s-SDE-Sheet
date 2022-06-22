# question: https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1

def maximumMeetings(n,start,end):
    li=[]
    res=[1]
    for i in range(n):
        li.append([start[i],end[i],i])
    li=sorted(li,key=lambda x:x[1])
    k=li[0][1]
    for i in range(1,len(li)):
        if li[i][0]>k:
            res.append(li[i][2]+1)
            k=li[i][1]
    return res

start = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
end =  [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]
print(maximumMeetings(len(start),start,end))
