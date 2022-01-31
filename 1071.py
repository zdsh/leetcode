class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1, len2 = len(str1), len(str2)
        if len1 < len2:
            str1, str2 = str2, str1
            len1, len2 = len(str1), len(str2)
        for i in range(len2, 0, -1):
            if len1 % i != 0 or len2 % i != 0:
                continue
            if str2[0:i] * (len1/i) == str1 and str2[0:i] * (len2/i) == str2:
                return str2[0:i]
        return '' 
