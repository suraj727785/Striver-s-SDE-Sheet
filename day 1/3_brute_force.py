def permutList(l):
    if not l:
            return [[]]
    res = []
    for e in l:
            temp = l[:]
            temp.remove(e)
            res.extend([[e] + r for r in permutList(temp)])

    return res

def nextPermutation(nums):
    res=permutList(nums)
    res.sort()
    for i in range(len(res)):
        if res[i]==nums:
            break
    if i==len(res)-1:
        return res[0]
    return res[i+1]
print(nextPermutation([3,2,1]))


    