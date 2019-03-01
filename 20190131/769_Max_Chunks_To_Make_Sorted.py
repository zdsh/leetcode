"""
File: 769_Max_Chunks_To_Make_Sorted.py
Date: 2019/03/01 10:19:44
"""
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        i, n, res = 0, len(arr), 0
        while i < n:
            j, seg, block_max = i + 1, i, arr[i]
            while j < n:
                if arr[j] < block_max:
                    block_max = max(block_max, max(arr[seg:j]))
                    seg = j
                j += 1
            res += 1
            i = seg + 1
        return res  
