# Question: https://leetcode.com/problems/sudoku-solver/

def solveSudoku(board):
    import math
    def isSafe(board,row,col,n,val):
        # for row
        for i in range(n):
            if board[i][col]==str(val):
                return False
        # for col
        for i in range(n):
            if board[row][i]==str(val):
                return False
        m=math.ceil((row+1)/3)*3-3
        n=math.ceil((col+1)/3)*3-3
        for i in range(m,m+3):
            for j in range(n,n+3):
                if board[i][j]==str(val):
                    return False
        return True
    n=len(board)
    def solve(board,n):
        for i in range(n):
            for j in range(n):
                if board[i][j]==".":
                    for k in range(1,10):
                        if isSafe(board,i,j,n,k):
                            board[i][j]=str(k)
                            if solve(board,n):
                                return True
                            else:
                                board[i][j]="."
                    return False
        return True
    solve(board,n)
    return board

board =[["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]
        
print(solveSudoku(board))


            
        
