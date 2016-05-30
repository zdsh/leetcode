class Solution(object):
    def dfs_path(self,i,j,matrix):
        r=len(matrix)
        c=len(matrix[0])
        ret=1
        if i-1>=0 and matrix[i][j]>matrix[i-1][j]:
            if self.path[i-1][j]==-1:
                self.path[i-1][j]=self.dfs_path(i-1,j,matrix)
            ret=max(ret,self.path[i-1][j]+1)
        if i+1<r and matrix[i][j]>matrix[i+1][j]:
            if self.path[i+1][j]==-1:
                self.path[i+1][j]=self.dfs_path(i+1,j,matrix)
            ret=max(ret,self.path[i+1][j]+1)
        if j-1>=0 and matrix[i][j]>matrix[i][j-1]:
            if self.path[i][j-1]==-1:
                self.path[i][j-1]=self.dfs_path(i,j-1,matrix)
            ret=max(ret,self.path[i][j-1]+1)                
        if j+1<c and matrix[i][j]>matrix[i][j+1]:
            if self.path[i][j+1]==-1:
                self.path[i][j+1]=self.dfs_path(i,j+1,matrix)
            ret=max(ret,self.path[i][j+1]+1) 
        return ret
        
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        r=len(matrix)
        if r<=0:
            return 0
        c=len(matrix[0])
        self.path=[]
        for i in range(0,r):
            self.path.append([])
            for j in range(0,c):
                self.path[i].append(-1)

        ret=-1
        for i in range(0,r):
            for j in range(0,c):
                if self.path[i][j]==-1:
                    self.path[i][j]=self.dfs_path(i,j,matrix)
                ret=max(ret,self.path[i][j])
                
        print(self.path)
        return ret
                    
