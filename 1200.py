class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        min_diff = arr[1] - arr[0]
        ret = []
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i-1])    
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_diff:
                ret.append([arr[i-1], arr[i]])
        return ret
        
