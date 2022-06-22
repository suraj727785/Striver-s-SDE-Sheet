# question: https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1

def maximumMeetings(n,start,end):
    start.sort()
    end.sort()
    i=j=0
    res=0
    while(i<n and j<n):
        res+=1
        if start[i]>end[j]:
            res-=1
            j+=1
        i+=1
    return res


start = [50,120,200,550,700,850]
end =  [500,550,600,700,900,1000]
print(maximumMeetings(len(start),start,end))
