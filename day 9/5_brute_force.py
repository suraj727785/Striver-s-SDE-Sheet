# Question: https://leetcode.com/problems/combination-sum-ii/


def palindromPartition(s,ind,r,res):
    if ind>=len(s):
        return
    if s[ind:]==s[ind:][::-1]:
        r.append(s[ind:])
        res.append(r[:])
        r.pop()
    for i in range(ind+1,len(s)):
        if s[ind:i]==s[ind:i][::-1]:
            r.append(s[ind:i])
            palindromPartition(s,i,r,res)
            r.pop()

    

s="aabb"
res=[]
palindromPartition(s,0,[],res)
print(res)
