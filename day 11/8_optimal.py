# Question: https://www.codingninjas.com/codestudio/problems/chess-tournament_981299/

def chessTournament(positions, n , c):
    def canPlace(positions,n,c,dist):
        cnt,fc=1,positions[0]
        for i in range(1,n):
            if positions[i]-fc>=dist:
                cnt+=1
                fc=positions[i]
            if cnt==c:
                return True
        return False

    positions.sort()
    low,high=1,positions[-1]-positions[0]
    res=-1
    while(low<=high):
        mid=(low+high)//2
        if canPlace(positions,n,c,mid):
            res=mid
            low=mid+1
        else:
            high=mid-1           
    return res



positions=[1, 2, 3, 4, 6]
n=5
c=3
print(chessTournament(positions,n,c))
