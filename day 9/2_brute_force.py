# Question: https://leetcode.com/problems/subsets-ii/
# used power set

def subsetsWithDup(nums):
    n=len(nums)
    res=[[]]
    nums.sort()
    print(nums)
    l=len(bin(pow(2,n)-1)[2:])
    for i in range(1,pow(2,n)):
        t=[int(x) for x in bin(i)[2:]]
        k=[0]*(l-len(t))+t
        r=[]
        print(k)
        for i in range(len(k)):
            if k[i]==1:
                print(i,"c")
                r.append(nums[i])
        print(r)
        if r not in res:
            res.append(sorted(r))
    
    return res

a=[1,2,2]
print(subsetsWithDup(a))