class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res={}
        for num in nums:
            if num not in res:
                res[num]=0
            res[num]+=1
        from operator import itemgetter
        res=sorted(res.iteritems(),key=itemgetter(1),reverse=True)
        r=[]
        for i in range(0,k):
            r.append(res[i][0])
        return r      

