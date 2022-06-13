def searchMatrix(matrix, target):
        for k in matrix:
            if target in k:
                return True
        return False
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))