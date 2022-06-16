# question: https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s):
    res=1
    if len(s)==0:
        return 0
    sett=set()
    l,r=0,0
    while(r<len(s) and l<len(s)):
        if s[r] not in sett:
            sett.add(s[r])
            if r-l+1>res:
                res=r-l+1
            r+=1
        else:
            sett.remove(s[l])
            l+=1           
    return res
print(lengthOfLongestSubstring("pwwkew"))
