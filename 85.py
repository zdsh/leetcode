class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        m=len(matrix)
        if m<=0:
            return 0
        n=len(matrix[0])
        
        height=[0]*n
        ret=0
        for i in range(m):
            if i==0:
                for j in range(n):
                    if matrix[i][j]=='1':
                        height[j]=1
            else:
                for j in range(n):
                    if matrix[i][j]=='1':
                        height[j]+=1
                    elif matrix[i][j]=='0':
                        height[j]=0
            
            stack=[0]
            for j in range(1,n):
                if height[j]>=height[stack[-1]]:
                    stack.append(j)
                else:
                    while len(stack)>0 and height[j]<height[stack[-1]]:
                        if len(stack)>1:
                            ret=max(ret,(j-1-stack[-2])*height[stack[-1]])
                        else:
                            ret=max(ret,j*height[stack[-1]])
                        del stack[-1]
                    stack.append(j)
            while len(stack)>0:
                if len(stack)>1:
                    ret=max(ret,(n-1-stack[-2])*height[stack[-1]])
                else:
                    ret=max(ret,n*height[stack[-1]])
                del stack[-1]
        return ret
                        
