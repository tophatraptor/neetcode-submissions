class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_values = '.123456789'
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] not in valid_values:
                    return False
                if board[row][col] == '.':
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] not in valid_values:
                    return False
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        
        for square in range(9):
            col = (square % 3) * 3
            row = 3 * (square // 3)
            seen = set()
            for i in range(3):
                for j in range(3):
                    if board[row + i][col + j] == '.':
                        continue
                    if board[row + i][col + j] not in valid_values:
                        return False
                    if board[row + i][col + j] in seen:
                        return False
                    seen.add(board[row + i][col + j])
        return True