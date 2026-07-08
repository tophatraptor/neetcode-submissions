class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        First, we need to find the row, so binary search on that
        """
        lower = 0
        upper = len(matrix) - 1
        while lower < upper:
            target_row = lower + (upper - lower) // 2
            if matrix[target_row][0] == target:
                return True
            if matrix[target_row][0] < target:
                if matrix[target_row][-1] >= target:
                    upper = target_row
                    lower = target_row
                else:
                    lower = target_row + 1
            else:
                upper = target_row - 1
        # Now, lower == upper and is target row
        target_row = lower
        lower = 0
        upper = len(matrix[target_row]) - 1
        while lower <= upper:
            target_col = lower + (upper - lower) // 2
            if matrix[target_row][target_col] == target:
                return True
            if matrix[target_row][target_col] < target:
                lower = target_col + 1
            else:
                upper = target_col - 1
        return False