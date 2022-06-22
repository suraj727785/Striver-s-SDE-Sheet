# question: https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1

class Item:
    def __init__(self,value,weight):
        self.id=id
        self.weight=weight
        self.value=value

def fractionalknapsack(W,Items,n):
    li=[]
    for i in range(n):
        li.append([Items[i].weight,Items[i].value,Items[i].value/Items[i].weight])
    li=sorted(li,reverse=True,key=lambda x:x[2])
    i=0
    res=0
    while(W>0 and i<len(li)):
        if li[i][0]<=W:
            W-=li[i][0]
            res+=li[i][1]
            i+=1
        else:
            res+=li[i][2]*W
            W=0
    return res



inputt=[[60,10], [100,20], [120,30]]
Items=[]
W=50
for i in range(len(inputt)):
    newItem=Item(inputt[i][0],inputt[i][1])
    Items.append(newItem)
print(fractionalknapsack(W,Items,len(Items)))
