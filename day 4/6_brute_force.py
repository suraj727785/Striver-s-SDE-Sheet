# question: https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s):
    res=1
    if len(s)==0:
        return 0
    for i in range(len(s)):
        li=[]
        count=0
        for j in range(i,len(s)):
            if s[j] not in li:
                li.append(s[j])
                count+=1
            else:
                if count>res:
                    res=count
                break
        if count>res:
            res=count
    return res
print(lengthOfLongestSubstring("abcabcbb"))
