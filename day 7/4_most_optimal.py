# question: https://leetcode.com/problems/trapping-rain-water/

def trap(height):
    res=0
    l,r,maxL,maxR=0,len(height)-1,0,0
    while(l<=r):
        if height[l]<=height[r]:
            if height[l]>=maxL:
                maxL=height[l]
            else:
                res+=maxL-height[l]
            l+=1
        else:
            if height[r]>=maxR:
                maxR=height[r]
            else:
                res+=maxR-height[r]
            r-=1
    return res

      
height=[4,2,0,3,2,5]
print(trap(height))
