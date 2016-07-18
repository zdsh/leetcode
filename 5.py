class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=1:
            return s
        max_len,ret=0,''
        for i in range(len(s)-1):
            j,k=i,i
            while j-1>=0 and k+1<len(s) and s[j-1]==s[k+1]:
                j-=1
                k+=1
            if k-j+1>max_len:
                max_len=k-j+1
                ret=s[j:k+1]
            
            j,k=i,i+1
            while j>=0 and k<len(s) and s[j]==s[k]:
                j-=1
                k+=1
            if k-j-1>max_len:
                max_len=k-j-1
                ret=s[j+1:k]
        return ret
            
