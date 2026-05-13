class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows*cols - 1

        while l <= r:
            m = l + (r-l)//2
            row, column = m//cols, m% cols

            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                l = m + 1
            else:
                r = m - 1
        return False