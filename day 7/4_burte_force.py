# question: https://leetcode.com/problems/trapping-rain-water/

def trap(height):
    res=0
    for i in range(len(height)):
        maxL=0
        maxR=0
        for j in range(0,i+1):
            if height[j]>maxL:
                maxL=height[j]
        for j in range(i,len(height)):
            if height[j]>maxR:
                maxR=height[j]
        if min(maxL,maxR)-height[i]>0:
            res+=min(maxL,maxR)-height[i]
    return res


      
height=[4,2,0,3,2,5]
print(trap(height))
