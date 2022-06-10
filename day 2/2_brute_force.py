def merge(intervals):
    intervals=sorted(intervals,key=lambda i:i[0])
    i=0
    while(i<len(intervals)-1):
        if intervals[i][1]>=intervals[i+1][0]:
            if intervals[i][1]>intervals[i+1][1]:
                intervals[i+1][1]=intervals[i][1]
            intervals[i+1][0]=intervals[i][0]
            intervals.pop(i)
        else:
            i+=1
    return intervals
print(merge([[1,4],[0,4]]))