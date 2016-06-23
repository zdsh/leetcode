class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret=[]
        res={}
        for s in strs:
            d={}
            for l in s:
                if l in d:
                    d[l]+=1
                else:
                    d[l]=1
            d=sorted(d.iteritems(),key=lambda x:x[0])
            k=str(d)
            if k in res:
                res[k].append(s)
            else:
                res[k]=[s]
        for k in res:
            ret.append(res[k])
        return ret
