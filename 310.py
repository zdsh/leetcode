class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n==1:
            return [0]
        adj_set=collections.defaultdict(lambda:set())
        for edge in edges:
            adj_set[edge[0]].add(edge[1])
            adj_set[edge[1]].add(edge[0])
        
        leaves=[k for k in adj_set if len(adj_set[k])==1]

        while n>2:
            n-=len(leaves)
            new_leaves=[]
            for leave in leaves:
                v=adj_set[leave].pop()
                adj_set[v].remove(leave)
                if len(adj_set[v])==1:
                    new_leaves.append(v)
            leaves=new_leaves
        return leaves
        
