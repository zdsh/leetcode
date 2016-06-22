class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        size=len(triangle)
        if size<=0:
            return 0
        res=[[triangle[i][j] for j in range(0,len(triangle[i]))] for i in range(0,size)]
        for i in range(size-2,-1,-1):
           for j in range(0,len(triangle[i])):
               res[i][j]=min(res[i+1][j],res[i+1][j+1])+triangle[i][j]
        return res[0][0]
