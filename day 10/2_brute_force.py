# Question: https://leetcode.com/problems/n-queens/
# should only check for upper diagonal, lower diagonal and row
def solveNQueens(n):
    def isSafe(board,row,col,n):
        dupRow=row
        dupCol=col
        # for upper diagonal
        while(row>=0 and col>=0):
            if board[row][col]=='Q':
                return False
            row-=1
            col-=1
        row=dupRow
        col=dupCol
        # for pervious space in row
        while(col>=0):
            if board[row][col]=='Q':
                return False
            col-=1
        row=dupRow
        col=dupCol
        # for upper diagonal
        while(row<n and col>=0):
            if board[row][col]=='Q':
                return False
            row+=1
            col-=1
        
        return True
    def solve(board,col,n,res):
        if col==n and board[:] not in res:
            res.append(board[:])
            return
        for row in range(n):
            if isSafe(board,row,col,n):
                board[row]=board[row][:col]+'Q'+board[row][col+1:]
                solve(board,col+1,n,res)
                board[row]=board[row][:col]+'.'+board[row][col+1:]
    s='.'*n
    board=[s for _ in range(n)]
    res=[]
    solve(board,0,n,res)
    return res

print(solveNQueens(4))


            
        
