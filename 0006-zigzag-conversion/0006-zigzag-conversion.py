class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = {i: [] for i in range(numRows)}
        row, step = 0, 1
        for ch in s:
            ans[row].append(ch)
            if row == 0:
                step = 1
            elif row == numRows-1:
                step = -1
            row += step
        return ''.join(''.join(ans[i]) for i in range(numRows))
