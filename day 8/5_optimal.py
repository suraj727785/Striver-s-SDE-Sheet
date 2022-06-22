# question: https://www.codingninjas.com/codestudio/problems/975277?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website

denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def findMinimumCoins(amount,dp):
    denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    i=len(denominations)-1
    if amount==0:
        return 0
    while(i>=0 and amount<denominations[i]):
        i-=1
    if dp[amount-denominations[i]]!=-1:
        return 1+dp[amount-denominations[i]]
    else:
        dp[amount-denominations[i]]=findMinimumCoins(amount-denominations[i],dp)
    return 1 + dp[amount-denominations[i]]
amount=49
dp=[-1 for _ in range(amount+1)]
print(findMinimumCoins(amount,dp))