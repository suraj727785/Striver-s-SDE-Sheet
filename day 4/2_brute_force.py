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
            print("2")
            l=j+1
            h=n-1
            while(l<h):
                print(li)
                if nums[l]+nums[h]==target-(nums[i]+nums[j]):
                    li.append([nums[i],nums[j],nums[l],nums[h]])
                    while(l<=h or nums[l]==nums[l+1]):
                        l+=1
                    while(l<=h or nums[h]==nums[h-1]):
                        h-=1 
                elif(nums[l]+nums[h]<target-(nums[i]+nums[j])):
                    while(l<=h or nums[l]==nums[l+1]):
                        l+=1
                else:
                    while(l<=h or nums[h]==nums[h-1]):
                        h-=1
            while(j<=n-2 or nums[j]==nums[j+1]):
                j+=1
        while(i<=n-3 or nums[i]==nums[i+1]):
            i+=1    
    return li
print(fourSum([1,0,-1,0,-2,2],0))