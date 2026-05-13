class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        toprow, bottomrow = 0, rows - 1

        while toprow <= bottomrow:
            row = (toprow + bottomrow)//2
            if target > matrix[row][-1]:
                toprow = row + 1
            elif target < matrix[row][0]:
                bottomrow = row - 1
            else:
                break
        
        if not (toprow <= bottomrow):
            return False

        row = (toprow + bottomrow)// 2
        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False


