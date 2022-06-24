# Question: https://leetcode.com/problems/permutation-sequence/


def getPermutation(n,k):
    n=[x for x in range(1,n+1)]
    # from question next permutation day 1 ques 3
    def permutList(l):
        if not l:
                return [[]]
        res = []
        for e in l:
                temp = l[:]
                temp.remove(e)
                res.extend([[e] + r for r in permutList(temp)])
        return res
    res=permutList(n)
    return ''.join([str(x) for x in res[k-1]])


print(getPermutation(4,9))