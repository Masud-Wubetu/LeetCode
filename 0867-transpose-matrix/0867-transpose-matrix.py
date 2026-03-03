class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        result = []
        
        for c in range(cols):
            new_row = []
            for r in range(rows):
                new_row.append(matrix[r][c])
            result.append(new_row)
        
        return result
