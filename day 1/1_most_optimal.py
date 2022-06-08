
def setZeroes(matrix):
    col=False
    for i in range(len(matrix)):
        if matrix[i][0]==0:
            col=True
        for j in range(1,len(matrix[0])):
            if matrix[i][j]==0:
                matrix[i][0]=0
                matrix[0][j]=0
    for i in range(len(matrix)-1,-1,-1):
        for j in range(len(matrix[0])-1,0,-1):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0
        if col:
            matrix[i][0]=0
    return matrix
print(setZeroes([[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]))