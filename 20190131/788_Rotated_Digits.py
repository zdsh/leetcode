"""
File: 788_Rotated_Digits.py
Date: 2019/03/02 10:49:23
"""
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 10:
            return sum([i in [2, 5, 6, 9] for i in range(N+1)])
        record = [4]
        i, b = 1, 10
        while b < N:
            record.append(record[-1] * 7 + 4 * pow(3, i))
            i, b = i + 1, b * 10

        ret, v, y = 0, int(str(N)[0]), N%(pow(10, len(str(N))-1))
        for i in range(v):
            if i in [0, 1, 8, 2, 5, 6]:
                ret += record[-2]
            if i in [2, 5, 6, 9]:
                ret += pow(3, len(str(N))-1)
        print ret

        if v in [1, 2, 5, 6, 8, 9]:
            ret += self.rotatedDigits(y)
        print ret

        def get_val(y):
            if y <= 9:
                return len([x for x in range(y+1) if x in [0, 1, 8]])
            ret = 0
            k = pow(3, len(str(y)) - 1)
            for f in range(int(str(y)[0])):
                if f in [0, 1, 8]:
                    ret += k
            if int(str(y)[0]) in [0, 1, 8]:
                ret += get_val(int(str(y)[1:]))
            return ret

        if v in [2, 5, 6, 9]:
            ret += get_val(y)
        return ret

if __name__ == '__main__':
    sol = Solution()
    print sol.rotatedDigits(516)
    print sol.rotatedDigits(16)
    print sol.rotatedDigits(1216)
    print '---'
    print sol.rotatedDigits(6121)
    print '---'
    print sol.rotatedDigits(991)
    exit(0)
    print sol.rotatedDigits(1000)
    print sol.rotatedDigits(54)
    print sol.rotatedDigits(154)
    print sol.rotatedDigits(888)
    print sol.rotatedDigits(516)
    print sol.rotatedDigits(8881)
    print sol.rotatedDigits(3578)
    
