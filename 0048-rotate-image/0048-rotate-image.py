class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.rev(matrix)
    def transpose(self, matrix):
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    def rev(self, matrix):
        for row in matrix:
            l, r = 0, len(row)-1
            while l<=r:
                row[l], row[r] = row[r], row[l]
                l+=1
                r-=1
            
