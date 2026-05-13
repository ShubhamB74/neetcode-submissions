class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows*cols - 1

        while l <= r:
            m = l + (r-1)//2
            r, c = m//cols, m% cols

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                l = m + 1
            else:
                r = m - 1
        return False