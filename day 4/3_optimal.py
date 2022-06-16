# question: https://leetcode.com/problems/longest-consecutive-sequence/

def longestConsecutive(nums):
    res=1
    if len(nums)==0:
        return 0
    sett=set(nums)
    for i in range(len(nums)):
        if nums[i]-1 in sett:
            continue
        else:
            r=nums[i]
            c=1
            while(True):
                if r+1 in sett:
                    c+=1
                    r+=1
                else:
                    if res<c:
                        res=c
                    break
    return res

print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
