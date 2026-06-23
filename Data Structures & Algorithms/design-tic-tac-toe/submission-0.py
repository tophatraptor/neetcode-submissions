class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[None for _ in range(n)] for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            token = 'X'
        else:
            token = 'O'
        
        self.board[row][col] = token
        n = self.n
        # Check if the board is in a winning state or not
        # Check vertically
        is_vertical_match = True
        is_horizontal_match = True
        for i in range(n):
            if self.board[i][col] != token:
                is_vertical_match = False
            if self.board[row][i] != token:
                is_horizontal_match = False
        # Check horizontally
        if row == col:
            # Need to check the top left to bottom right diagonal
            is_diag1_match = True
            for i in range(n):
                if self.board[i][i] != token:
                    is_diag1_match = False
        else:
            is_diag1_match = False
        if row + col == n-1:
            is_diag2_match = True
            for i in range(n):
                # row = i
                # col = n - i - 1
                if self.board[n - i - 1][i] != token:
                    is_diag2_match = False
        else:
            is_diag2_match = False
        
        if is_horizontal_match or is_vertical_match or is_diag1_match or is_diag2_match:
            return player
        return 0

        # If the tic tac toe is placed where row == col
        # Or on the other diagonal axis, row + col = n - 1


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
