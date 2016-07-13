class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        def solve(ratings):
            if len( ratings ) <= 0:
                return []
            if len( ratings ) == 1:
                return [1]
            n=len(ratings)
            ret=[1]*n
            min_val=min(ratings)
            i=ratings.index(min_val)
            pre,next=i-1,i+1
            while pre>=0 and ratings[pre]>=ratings[pre+1]:
                if ratings[pre]==ratings[pre+1]:
                    ret[pre]=1
                else:
                    ret[pre]=ret[pre+1]+1
                pre-=1
            if pre>=0:
                ret[0:pre+1]=solve(ratings[0:pre+1])
            while next<n and ratings[next]>=ratings[next-1]:
                if ratings[next]==ratings[next-1]:
                    ret[next]=1
                else:
                    ret[next]=ret[next-1]+1
                next+=1
            if next<=n-1:
                ret[next:]=solve(ratings[next:])
            if pre>=0:
                ret[pre+1]=max(ret[pre]+1,ret[pre+1])
            if next<n:
                ret[next-1]=max(ret[next]+1,ret[next-1])
            return ret
        return sum(solve(ratings))
            
