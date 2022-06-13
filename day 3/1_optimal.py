def searchMatrix(matrix,target):
            n,m=len(matrix),len(matrix[0])
            l,r=0,(n*m)-1
            while l <= r:
                mid = l + (r - l) // 2
                if matrix[mid//m][mid%m] == target:
                    return True
                elif matrix[mid//m][mid%m] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))