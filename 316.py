class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s=='':
            return ''
        res=collections.defaultdict(lambda:0)
        for letter in s:
            res[letter]+=1
        pos=0
        for j in range(0,len(s)):
            l=s[j]
            res[l]-=1
            if s[pos]>s[j]:
                pos=j
            if res[l]==0:
                return s[pos]+self.removeDuplicateLetters(s[pos+1:].replace(s[pos],''))
            j+=1

