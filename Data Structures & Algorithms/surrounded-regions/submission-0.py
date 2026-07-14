class Solution:
    def solve(self, board: List[List[str]]) -> None:
        stack = []
        m = len(board)
        n = len(board[0])
        for i in range(m):
            if board[i][0] == 'O':
                stack.append([i, 0])
            if board[i][n-1] == 'O':
                stack.append([i, n-1])
        for j in range(n):
            if board[0][j] == 'O':
                stack.append([0, j])
            if board[m-1][j] == 'O':
                stack.append([m-1, j])
        
        while len(stack) > 0:
            res = stack.pop()
            r = res[0]
            c = res[1]
            # If we already visited
            if board[r][c] == 'I':
                continue
            board[r][c] = 'I'
            neighbors = self.gen_neighbors(r, c, m, n)
            for neighbor in neighbors:
                if board[neighbor[0]][neighbor[1]] == 'O':
                    stack.append(neighbor)
        
        # At this juncture, all border regions should be 'I'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'I':
                    board[i][j] = 'O'
        
            
    
    def gen_neighbors(self, x, y, m, n):
        res = []
        if x-1 >= 0:
            res.append([x-1, y])
        if y-1 >= 0:
            res.append([x, y-1])
        if x+1 < m:
            res.append([x + 1, y])
        if y + 1 < n:
            res.append([x, y+1])
        
        return res


"""
We can solve this with BFS or DFS; all we have to do is iterate over all border cells
And mark those border cells + their neighbors based on traversal as immune ('I')

Then we traverse over the board twice. The first time, we're going to mark all 'O's
as 'X's, then convert all 'I's to 'O's after. This gives  us a mxn runtime.
"""