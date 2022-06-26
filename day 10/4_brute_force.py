# Question: https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1#
def graphColoring(graph, k, V):
    def isSafe(node,graph,color,i):
        for j in range(len(graph[node])):
            if j!=node and graph[node][j]==1 and color[j]==i:
                return False
        return True

    def solve(graph,color,k,V,node):
        if node==V:
            return True
        for i in range(1,k+1):
            if isSafe(node,graph,color,i):
                color[node]=i
                if solve(graph,color,k,V,node+1):
                    return True
                color[node]=0
        return False
    color=[0 for _ in range(V)]
    return solve(graph,color,k,V,0)

graph=[[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
k,V=3,4
print(graphColoring(graph,k,V))



            
        
