def setZeroes(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    for k in range(len(matrix)):
                        if matrix[k][j]!=0:
                            matrix[k][j]=-1
                    for k in range(len(matrix[0])):
                        if matrix[i][k]!=0:
                            matrix[i][k]=-1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==-1:
                    matrix[i][j]=0
        return matrix
print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))