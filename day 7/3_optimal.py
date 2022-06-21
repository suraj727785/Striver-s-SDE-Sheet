# question: https://leetcode.com/problems/3sum/

def threeSum(nums):
    nums.sort()
    res=[]
    i=0
    while i<(len(nums)-2):
        j,k=i+1,len(nums)-1
        while(j<k):
            print(nums[i],nums[j],nums[k])
            if nums[j]+nums[k]==-(nums[i]):
                res.append([nums[i],nums[j],nums[k]])
                j+=1
                while(j<k and nums[j]==nums[j-1]):
                    j+=1
                while(j<k and nums[k]==nums[k-1]):
                    k-=1
            elif nums[j]+nums[k]<-(nums[i]): 
                j+=1
                while(j<k and nums[j]==nums[j-1]):
                    j+=1
            else:
                k-=1
                while(j<k and nums[k]==nums[k+1]):
                    k-=1
        i+=1
        while(i<(len(nums)-2) and nums[i]==nums[i-1]):
            i+=1
    return res
      
a=[-1,0,1,2,-1,-4]
print(threeSum(a))
