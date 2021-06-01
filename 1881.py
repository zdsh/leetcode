class Solution(object):
    def maxValue(self, n, x):
        """
        :type n: str
        :type x: int
        :rtype: str
        """
        v = int(n)
        if v > 0:
            for i in range(0, len(n)):
                if int(n[i]) < x:
                   return n[0:i] + str(x) + n[i:]
        else:
             for i in range(1, len(n)):
                if int(n[i]) > x:
                   return n[0:i] + str(x) + n[i:]
        return n + str(x)
