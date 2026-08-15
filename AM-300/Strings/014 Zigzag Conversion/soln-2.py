class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curr_row = 0
        step = 1  # Direction: 1 for down, -1 for up

        for char in s:
            rows[curr_row] += char
            
            # Reverse direction at boundaries
            if curr_row == 0:
                step = 1
            elif curr_row == numRows - 1:
                step = -1
                
            curr_row += step

        return "".join(rows)
# Row Simulation / Direction Toggle
# time -> O(n)
# space -> O(n)