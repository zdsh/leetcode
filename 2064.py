class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """
        s, e = 1, max(quantities)
        while s < e:
            dividor, c = (s+e)/2,  0
            for q in quantities:
                c += (q + dividor - 1) / dividor
            if c <= n:
                e = dividor
            else:
                s = dividor + 1
        return (s+e)/2
