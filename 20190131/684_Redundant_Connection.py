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
                x = parent[x]
            return x
        
        def union(x, y):
            parent[find(y)] = find(x)
        
        for edge in edges:
            if find(edge[0]) == find(edge[1]):
                return edge
            union(edge[0], edge[1])
