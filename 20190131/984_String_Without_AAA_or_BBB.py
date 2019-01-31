"""
File: 984_String_Without_AAA_or_BBB.py
Date: 2019/01/31 10:55:48
"""

class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        ret = ''
        if B > 2 * A + 2 or A > 2 * B + 2:
             return ret
        if A == 0:
             return 'b' * B
        if B == 0:
             return 'a' * A

        if A <= B:
            left_A, left_B = A, B
            while left_B > left_A:
                ret += 'bba'
                left_B -= 2
                left_A -= 1
            while left_B > 0 and left_A > 0:
                ret += 'ba'
                left_B -= 1
                left_A -= 1
            if left_A > 0:
                ret += 'a' * left_A
            return ret

        if A > B:
            left_A, left_B = A, B
            while left_B < left_A:
                ret += 'aab'
                left_B -= 1
                left_A -= 2
            while left_B > 0 and left_A > 0:
                ret += 'ab'
                left_B -= 1
                left_A -= 1
            if left_B > 0:
                ret += 'b' * left_B
            return ret

if __name__ == '__main__':
    solution = Solution()
    print solution.strWithout3a3b(1, 2)
    print solution.strWithout3a3b(4, 1)
    print solution.strWithout3a3b(4, 1)
    print solution.strWithout3a3b(10, 1)
    print solution.strWithout3a3b(4, 3)
