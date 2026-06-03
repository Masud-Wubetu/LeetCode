class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [""] * numRows
        
        curr = 0
        dire = 1

        for c in s:
            
            rows[curr] += c

            if curr == 0:
                dire = 1
            elif curr == numRows - 1:
                dire = -1
            
            curr += dire
        
        return "".join(rows)