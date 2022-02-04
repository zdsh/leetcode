class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        ret = [[t] for t in range(1,10)]
        for j in range(1, n):
            ret_ = []
            for r in ret:
                if r[-1] + k < 10:
                    ret_.append([n for n in r] + [r[-1] + k])
                if r[-1] + k == r[-1] - k:
                    continue
                if r[-1] - k >= 0:
                    ret_.append([n for n in r] + [r[-1] - k])
            ret = [r for r in ret_]
        return [int(''.join(map(str, item))) for item in ret]  
