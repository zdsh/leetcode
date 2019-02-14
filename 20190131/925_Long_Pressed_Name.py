"""
File: 925_Long_Pressed_Name.py
Date: 2019/02/14 11:31:19
"""
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if len(typed) < len(name):
             return False
        i, j = 0, 0
        while i < len(name) and j < len(typed):
            c_n, c_t = 1, 1
            n, t = name[i], typed[j]
            if n != t:
                return False
            while i < len(name) - 1 and name[i] == name[i+1]:
                c_n += 1
                i += 1
            while j < len(typed) - 1 and typed[j] == typed[j+1]:
                c_t += 1
                j += 1
            if c_n > c_t:
                return False
            i += 1
            j += 1
        if i == len(name) and j == len(typed):
            return True        
        return False
