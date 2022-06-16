# question: https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s):
    res=1
    if len(s)==0:
        return 0
    dic={}
    l,r=0,0
    while(r<len(s)):
        if s[r] in dic.keys():
            l=max(dic[s[r]]+1,l)
        dic[s[r]]=r
        if r-l+1>res:
            res=r-l+1  
        r+=1       
    return res
print(lengthOfLongestSubstring("pwwkew"))
