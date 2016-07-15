class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        def solve(s):
            i,l=0,0
            ret,start=0,0
            while i<len(s):
                if s[i]=='(':
                    l+=1
                elif s[i]==')':
                    if l<=0:
                        l=0
                        start=i+1
                    else:
                        l-=1
                        if l==0:
                            ret=max(i+1-start,ret)
                i+=1
            if l==0:
                ret=max(i-start,ret)
            return ret
        ret=0
        ret=max(solve(s),ret)
        s=s.replace('(','*')
        s=s.replace(')','(')
        s=s.replace('*',')')
        s=s[::-1]
        ret=max(solve(s),ret)
        return ret
