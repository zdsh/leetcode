class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_s=list(s)
        n=len(s)
        i=0
        j=n-1
        while i<j:
            list_s[i],list_s[j]=list_s[j],list_s[i]
            i+=1
            j-=1
        res=''.join(list_s)
        return res
