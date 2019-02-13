"""
File: 913_Cat_and_Mouse.py
Date: 2019/02/13 17:27:41
"""
class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        N = len(graph)
        def parents(m, c, t):
            ret = []
            if t == 2:
                for pre_m in graph[m]:
                    ret.append((pre_m, c, 1))
            else:
                for pre_c in graph[c]:
                    if pre_c:
                        ret.append((m, pre_c, 2))
            return ret

        DRAW, MOUSE, CAT = 0, 1, 2
        queue = collections.deque()
        color = collections.defaultdict(int)
        
        for i in range(0, N):
            for t in range(1, 3): 
                color[0, i, t] = MOUSE
                queue.append((0, i, t, MOUSE))
                if i > 0:
                    color[i, i, t] = CAT
                    queue.append((i, i, t, CAT))
        degree = {}
        for m in range(0, N):
            for c in range(0, N):
                degree[m, c, 1] = len(graph[m])
                degree[m, c, 2] = len(graph[c]) - ( 0 in graph[c])

        while queue:
            m, c, t, r = queue.popleft()
            for state in parents(m, c, t):
                pre_m, pre_c, pre_t = state
                if color[pre_m, pre_c, pre_t] == DRAW:
                    if pre_t == r:
                        color[pre_m, pre_c, pre_t] = r
                        queue.append((pre_m, pre_c, pre_t, r))
                    else:
                        degree[pre_m, pre_c, pre_t] -= 1
                        if degree[pre_m, pre_c, pre_t] == 0:
                            color[pre_m, pre_c, pre_t] = 3 - pre_t
                            queue.append((pre_m, pre_c, pre_t, 3 - pre_t)) 
                        
        return color[1, 2, 1]       
