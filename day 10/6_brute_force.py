# Question: https://www.codingninjas.com/codestudio/problems/983635
def wordBreakHelper(s, ind, dic, size):
    if (ind == size):
        return [""]

    subPart, completePart = [], []
    word = ""
    for j in range(ind, size):
        word += s[j]
        if (word not in dic):
            continue
        subPart = wordBreakHelper(s, j + 1, dic, size)
        for i in range(len(subPart)):
            if (len(subPart[i]) != 0):
                subPart[i] = word + " " + subPart[i]
            else:
                subPart[i] = word
        for i in range(len(subPart)):
            completePart.append(subPart[i])
    return completePart


def wordBreak(s, dictionary):
    dic = set()

    for i in range(len(dictionary)):
        dic.add(dictionary[i])

    return wordBreakHelper(s, 0, dic, len(s))
dictionary=["god", "is", "now", "no", "where", "here"]
s="godisnowherenowhere"
print(wordBreak(s,dictionary))
