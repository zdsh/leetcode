class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ret=0
        res=[]
        n=len(heights)
        for i in range(0,n):

            if len(res)==0:
                res.append(i)
            elif heights[i]>=heights[res[-1]]:
                res.append(i)
            else:
                while len(res)>0 and heights[res[-1]]>heights[i]:
                    if len(res)>1:
                        ret=max(ret,(i-1-res[-2])*heights[res[-1]])
                    else:
                        ret=max(ret,(i-0)*heights[res[-1]])
                    del res[-1]
                res.append(i)
        while len(res)>0:
            if len(res)>1:
                ret=max(ret,(n-1-res[-2])*heights[res[-1]])
            else:
                ret=max(ret,(n-0)*heights[res[-1]])
            del res[-1]       
        return ret
                
     
