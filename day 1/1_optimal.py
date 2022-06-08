def setZeroes(matrix):
    r=[1]*len(matrix)
    c=[1]*len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                r[i]=0
                c[j]=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if r[i]==0 or c[j]==0:
                matrix[i][j]=0
    return matrix
print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))