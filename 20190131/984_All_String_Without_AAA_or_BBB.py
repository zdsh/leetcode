"""
File: 984_String_Without_AAA_or_BBB.py
Date: 2019/01/31 10:55:48
"""

class Solution(object):
    recode = []
    for i in range(0, 101):
        recode.append([-1]*101)

    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        if self.recode[A][B] != -1:
            return self.recode[A][B]
        if A == 0:
            self.recode[A][B] = ['b' * B]
            return self.recode[A][B]
        if B == 0:
            self.recode[A][B] = ['a' * A]
            return self.recode[A][B]
        if A == 1:
            ret = []
            if B <= 5:
                for i in range(0, B+1):
                    if i <= 2 and B-i <= 2:
                        ret.append('b'*i + 'a' + 'b'*(B-i))
            self.recode[A][B] = ret
            return self.recode[A][B]
            
        if B == 1:
            ret = []
            if A <= 5:
                for i in range(0, A+1):
                    if i <= 2 and A-i <= 2:
                        ret.append('a'*i + 'b' + 'a'*(A-i))
            self.recode[A][B] = ret
            return self.recode[A][B]

        ret1 = self.strWithout3a3b(A, B-1)
        ret2 = self.strWithout3a3b(A-1, B)
        ret = []
        for v in ret1:
            if len(v) >= 2 and v[0] == 'b' and v[1]== 'b':
                continue
            else:
                ret.append('b' + v)
        for v in ret2:
            if len(v) >=2 and v[0] == 'a' and v[1] == 'a':
                continue
            else:
                ret.append('a' + v)
        self.recode[A][B] = ret
        return self.recode[A][B]

if __name__ == '__main__':
    solution = Solution()
    print solution.strWithout3a3b(1, 2)
    print solution.strWithout3a3b(4, 1)
    print solution.strWithout3a3b(4, 1)
    print solution.strWithout3a3b(10, 1)
    print solution.strWithout3a3b(4, 3)
