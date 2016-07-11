class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res=collections.defaultdict(lambda:0)
        for l in t:
            res[l]+=1
        n=len(s)
        b,e,counter=0,0,len(t)
        m=n+1
        ret=''
        for i in range(0,n):
            if s[i] in res:
                res[s[i]]-=1
                if res[s[i]]>=0:
                    counter-=1
            while counter==0:
                if i-b+1<m:
                    m=i-b+1
                    ret=s[b:i+1]
                if s[b] in res:
                    res[s[b]]+=1
                    if res[s[b]]>0:
                        counter+=1
                b+=1
            i+=1
        return ret
        
