from crio.io import PrintMatrix

class Solution:
    def __init__(self, matrix):
        self.matrix = matrix
# 1 2 3
# 4 5 6
# 7 8 9
# ---------
# 1 4 7
# 2 5 8
# 3 6 9
    def rotateImage(self):
        N=len(self.matrix)
        for i in range(N):
            for j in range(i):
                temp=self.matrix[i][j]
                self.matrix[i][j]=self.matrix[j][i]
                self.matrix[j][i]=temp
        for i in range(N):
            for j in range(N//2):
                temp=self.matrix[i][j]
                self.matrix[i][j]=self.matrix[i][N-1-j]
                self.matrix[i][N-1-j]=temp
if __name__ == '__main__':
    n = int(input())
    matrix = []
    for i in range(n):
        nums = input().split()
        nums = [int(i) for i in nums]
        matrix.append(nums)
    sol = Solution(matrix)
    sol.rotateImage()
    PrintMatrix.SquareMatrix(sol.matrix)

