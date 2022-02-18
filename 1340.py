class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        n = len(arr)
        views = [-1] * n
        def dp(i):
            if views[i] != -1:
                return views[i]
            ret = 1
            for x in range(1, d+1):
                if i+x >= n or arr[i+x] >= arr[i]:
                    break
                ret = max(dp(i+x)+1, ret)
            for x in range(1, d+1):
                if i-x < 0 or arr[i-x] >= arr[i]:
                    break
                ret = max(dp(i-x)+1, ret)
            views[i] = ret
            return ret
        for i in range(n):
            dp(i)
        return max(views)        
