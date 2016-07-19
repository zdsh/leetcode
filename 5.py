‘’’
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss='#'
        for l in s:
           ss+=l+'#'
        res=[0]*len(ss)
        c,r,i=0,0,1
        l,ret=0,''
        while i<len(ss)-1:
            if i<c+r:
                res[i]=min(c+r-i,res[2*c-i])
            else:
                res[i]=0
            j,k=i-res[i]-1,i+res[i]+1
            while j>=0 and k<len(ss) and ss[j]==ss[k]:
                j-=1
                k+=1
            res[i]=i-j-1
            if res[i]>l:
                l=res[i]
                ret=ss[i-res[i]:i+res[i]+1].replace('#','')
            if i+res[i]>c+r:
                c=i
                r=res[i]
            i+=1
        return ret
‘’’

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
            
