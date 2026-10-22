class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        while matrix and matrix[0]:
            ans.extend(matrix.pop(0))
            for row in matrix:
                ans.append(row.pop())
            if matrix and matrix[0]: ans.extend(matrix.pop()[::-1])
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ans.append(row.pop(0))
        return ans
