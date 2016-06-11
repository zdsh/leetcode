class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        s_e=sorted(envelopes,cmp=lambda x,y:x[0]-y[0] if x[0]!=y[0] else y[1]-x[1])
        size=len(s_e)
        print(s_e)
        dp=[]
        for i in range(0,size):
            low,high=0,len(dp)-1
            while low<=high:
                mid=(low+high)/2
                if dp[mid][1]<s_e[i][1]:
                    low=mid+1
                else:
                    high=mid-1
            if low<len(dp):
                dp[low]=s_e[i]
            else:
                dp.append(s_e[i])
        return len(dp)
        
