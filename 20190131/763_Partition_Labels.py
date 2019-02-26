class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n, res = len(S), {}
        for i in range(0, n):
            res[S[i]] = i
        
        s, e, ret = 0, res[S[0]], []
        for i in range(0, n):
            if i <= e:
                e = max(res[S[i]], e)
            else:
                ret.append(e + 1 - s)
                s, e = i, res[S[i]]
        ret.append(e + 1 - s)
        return ret
