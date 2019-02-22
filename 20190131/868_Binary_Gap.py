"""
File: 868_Binary_Gap.py
Date: 2019/02/22 14:53:23
"""
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        ret, binN = 0, bin(N)[2:]
        i, last = 0, -1
        
        while i < len(binN):   
            if binN[i] == '1':
                if last != -1:
                    ret = max(i - last, ret)
                last = i
            i += 1
        return ret
