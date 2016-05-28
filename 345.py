class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        j=len(s)-1
        n=len(s)
        res=[k for k in s]
        vowels=['a','e','i','o','u','A','E','I','O','U']
        while i<j:
            while i<n and s[i] not in vowels:
                i+=1
            while j>=0 and s[j] not in vowels:
                j-=1
            if i<j:
                res[i],res[j]=res[j],res[i]
                i+=1
                j-=1
        return ''.join(res)
            
            
