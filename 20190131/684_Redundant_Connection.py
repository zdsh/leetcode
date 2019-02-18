"""
File: 684_Redundant_Connection.py
Date: 2019/02/17 10:09:42
"""
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
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
