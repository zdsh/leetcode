class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.sums=matrix[:][:]
        m=len(matrix)
        if m<=0:
            return
        n=len(matrix[0])
        for i in range(1,m):
            self.sums[i][0]+=self.sums[i-1][0]
        for j in range(1,n):
            self.sums[0][j]+=self.sums[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                self.sums[i][j]+=self.sums[i-1][j]+self.sums[i][j-1]-self.sums[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        val=self.sums[row2][col2]
        if row1>0:
            val-=self.sums[row1-1][col2]
        if col1>0:
            val-=self.sums[row2][col1-1]
        if row1>0 and col1>0:
            val+=self.sums[row1-1][col1-1]
        return val

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
