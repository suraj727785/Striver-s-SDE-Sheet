def minHeap(N,Q):   
    def minHeapify(i,li):
        l = 2*i+1
        r = 2*i+2
        smallest = i
        if l < len(li) and li[l] < li[i]:
            smallest = l
        if r < len(li) and li[r] < li[i]:
            smallest = r
        if smallest != i:
            li[i],li[smallest]=li[smallest],li[i]
            minHeapify(smallest)
    li=[]
    res=[]
    for i in range(N):
        if len(Q[i])==1:
            res.append(li.pop(0))
            minHeapify(0,li)
        else:
            li.append(Q[i][1])
            i=len(li)-1
            while (i != 0 and li[(i-1)//2] > li[i]):
                li[i],li[(i-1)//2]=li[(i-1)//2],li[i]
                i =(i-1)//2
    return res

N=3
Q=[[0, 2,],[0, 1],[1]]
print(minHeap(N,Q))
