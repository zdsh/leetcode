"""
File: 952_Largest_Component_Size_by_Common_Factor.py
Date: 2019/02/16 21:51:14
"""
class Solution(object):
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        parent = {}
        def find(x):
            while x in parent and parent[x] != x:                
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px = find(x)
            py = find(y)
            parent[px] = py
            parent[py] = py

        for a in A:
            for f in range(2, int(math.sqrt(a)) + 1):
                if a % f == 0:
                    union(a, f)
                    union(a, a / f)
        counter = collections.defaultdict(int)
        for a in A:
            counter[find(a)] += 1
        return max(counter.values())
