class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        n=len(buildings)
        if n<=0:
            return []
        if n==1:
            return [[buildings[0][0],buildings[0][2]],[buildings[0][1],0]]
        left=self.getSkyline(buildings[0:n/2])
        right=self.getSkyline(buildings[n/2:])
        
        ret=[]
        lh,rh=None,None
        i,j=0,0
        while i<len(left) and j<len(right):
            if left[i][0]<right[j][0]:
                lh=left[i][1]
                if len(ret)==0 or ret[-1][1]!=max(lh,rh):
                    ret.append([left[i][0],max(lh,rh)])
                i+=1
            elif left[i][0]>right[j][0]:
                rh=right[j][1]
                if len(ret)==0 or ret[-1][1]!=max(lh,rh):
                    ret.append([right[j][0],max(lh,rh)])
                j+=1
            else:
                lh,rh=left[i][1],right[j][1]
                if len(ret)==0 or ret[-1][1]!=max(lh,rh):
                    ret.append([left[i][0],max(lh,rh)])
                i+=1
                j+=1
        while i<len(left):
            if len(ret)==0 or ret[-1][1]!=left[i][1]:
                ret.append(left[i][:])
            i+=1
        while j<len(right):
            if len(ret)==0 or ret[-1][1]!=right[j][1]:
                ret.append(right[j][:])
            j+=1
        return ret
