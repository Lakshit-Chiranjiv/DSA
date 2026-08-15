class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        res = []
        cycle = 2 * numRows - 2

        for row in range(numRows):
            for i in range(row, len(s), cycle):
                res.append(s[i])
                climb_idx = i + cycle - 2 * row
                if row != 0 and row != numRows - 1 and climb_idx < len(s):
                    res.append(s[climb_idx])

        return "".join(res)
# Direct Index Calculation
# time -> O(n)
# space -> O(n)