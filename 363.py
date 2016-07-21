class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m=len(matrix)
        if m<=0:
            return 0
        n=len(matrix[0])

        ret=None
        res=[ [v for v in row ] for row in matrix]

        for i in range(0,m):
            for j in range(1,n):
                res[i][j]+=res[i][j-1]
        
        for i in range(0,n):
            for j in range(i,n):
                s=0
                array=[]
                for t in range(m):
                    if i==0:
                        s+=res[t][j]
                    else:
                        s+=res[t][j]-res[t][i-1]
                        
                    p=bisect.bisect_left(array,s-k)
                    if s<=k:
                        ret=max(ret,s)
                    if p<len(array):
                        ret=max(ret,s-array[p])
                    bisect.insort(array,s)
        if ret==None:
            ret=0
        return ret
