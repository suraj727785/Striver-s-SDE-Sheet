# question : https://leetcode.com/problems/4sum/
def fourSum(nums,target):
    nums.sort()
    li=[]
    n=len(nums)
    print(nums)
    i=0
    while(i<n-3):
        j=i+1
        while(j<n-2):
            l=j+1
            h=n-1
            while(l<h):
                if nums[l]+nums[h]==(target-(nums[i]+nums[j])):
                    li.append([nums[i],nums[j],nums[l],nums[h]])
                    l+=1
                    while(l<h and nums[l]==nums[l-1]):
                        l+=1
                    while(l<h and nums[h]==nums[h-1]):
                        h-=1
                elif(nums[l]+nums[h]<target-(nums[i]+nums[j])):
                    l+=1
                    while(l<h and nums[l]==nums[l-1]):
                        l+=1
                else:
                    h-=1
                    while(l<h and nums[h]==nums[h+1]):
                        h-=1
            j+=1
            while(j<n-2 and nums[j]==nums[j-1]):
                j+=1
        i+=1
        while(i<n-3 and nums[i]==nums[i-1]):
            i+=1    
    return li
print(fourSum([1,0,-1,0,-2,2],0))