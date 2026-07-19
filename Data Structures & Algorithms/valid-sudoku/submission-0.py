class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            numbers = set()
            for j in range(9):
                if board[i][j] in numbers:
                    return False
                if board[i][j] != ".":
                    numbers.add(board[i][j]) 
        
        for i in range(9):
            numbers = set()
            for j in range(9):
                if board[j][i] in numbers:
                    return False
                if board[j][i] != ".":
                    numbers.add(board[j][i]) 
        
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                numbers = set()
                for left in range(i, i + 3):
                    for right in range(j, j + 3):
                        if board[left][right] in numbers:
                            return False
                        if board[left][right] != ".":
                            numbers.add(board[left][right])
    
        return True

            