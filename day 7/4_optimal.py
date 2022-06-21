# question: https://leetcode.com/problems/trapping-rain-water/

def trap(height):
    res=0
    maxL=[]
    maxR=[]
    for i in range(len(height)):
        if len(maxL)==0 or height[i]>maxL[-1]:
            maxL.append(height[i])
        else:
            maxL.append(maxL[-1])
    for i in range(len(height)-1,-1,-1):
        if len(maxR)==0 or height[i]>maxR[0]:
            maxR.insert(0,height[i])
        else:
            maxR.insert(0,maxR[0])
    for i in range(len(height)):
        if min(maxL[i],maxR[i])-height[i]>0:
            res+=min(maxL[i],maxR[i])-height[i]
    return res


      
height=[4,2,0,3,2,5]
print(trap(height))
