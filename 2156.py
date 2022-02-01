class Solution(object):
    def subStrHash(self, s, power, modulo, k, hashValue):
        """
        :type s: str
        :type power: int
        :type modulo: int
        :type k: int
        :type hashValue: int
        :rtype: str
        """
        value = 0
        if power % modulo != 0:
            power = power % modulo
        coff = 1
        for i in range(0, k):
            coff = coff if i == 0 else coff * power
            value += coff * (ord(s[i]) - ord('a') + 1)
        if value % modulo == hashValue:
            return s[0:k]

        for i in range(k, len(s)):
            value -= ord(s[i-k]) - ord('a') + 1
            value = value / power
            value += coff * (ord(s[i]) - ord('a') + 1)
            if value % modulo == hashValue:
                return s[i-k+1:i+1]        
