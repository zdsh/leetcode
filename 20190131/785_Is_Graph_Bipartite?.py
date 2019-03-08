"""
File: 785_Is_Graph_Bipartite?.py
Date: 2019/03/08 11:38:26
"""
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        findset = {}
        def union(x, y):
            findset[find(y)] = find(x)

        def find(x):
            if x not in findset:
                findset[x] = x
            while findset[x] != x:
                x = findset[x] 
            return x

        res = {}
        for i in range(0, len(graph)):
            nodes = graph[i]
            if len(nodes) <= 0:
                continue
            for x, y in zip(nodes, nodes[1:]):
                union(x, y) 
            res[i] = nodes[0]
        for x in res:
            if find(x) == find(res[x]):
                return False
        return True
