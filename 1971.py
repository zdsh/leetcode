class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        rec = {}
        for edge in edges:
            [a, b] = edge
            if a not in rec:
                rec[a] = set()
            rec[a].add(b)
            if b not in rec:
                rec[b] = set()
            rec[b].add(a)
        visited = {source:1}
        q = [source]
        while q:
            v = q.pop()
            if v == destination:
                return True
            if v not in rec:
                continue
            for e in rec[v]:
                if e not in visited:
                    visited[e] = 1
                    q += [e]
        return False        
