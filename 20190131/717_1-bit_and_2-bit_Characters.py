"""
File: 717_1-bit_and_2-bit_Characters.py
Date: 2019/03/19 22:26:07
"""
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if bits[-1] == 1:
            return False
        i, n = 0, len(bits)
        while i < n - 1:
            i = i + 2 if bits[i] == 1 else i + 1
        return True if i == n - 1 else False        
