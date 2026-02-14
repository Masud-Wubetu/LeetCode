class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = len(matrix)
        col = len(matrix[0])

        r = 0
        c = col - 1

        while r < row and c >= 0:

            current = matrix[r][c]

            if current == target:
                return True
            elif current < target:
                r += 1
            else:
                c -= 1
        
        return False