class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        i,j=0,n-1
        while j>=0:
            if s[i]==s[j]:
                i+=1
            j-=1
        if i==n:
            return s
        return s[i:][::-1]+self.shortestPalindrome(s[0:i])+s[i:]
