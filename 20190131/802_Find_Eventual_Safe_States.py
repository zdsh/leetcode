"""
File: 802_Find_Eventual_Safe_States.py
Date: 2019/03/11 19:49:13
"""
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n, final_node = len(graph), {}
        for i in range(n):
            if len(graph[i]) == 0:
                final_node[i] = i
        change = True
        while change:
            change = False
            for i in range(n):
                if not i in final_node:
                    edges = graph[i]
                    if all([v in final_node for v in edges]):
                        final_node[i] = i
                        change = True
        return sorted([k for k in final_node if final_node[k] >= 0])        

if __name__ == '__main__':
    solution = Solution()
    graph = [[],[0,2,3,4],[3],[4],[]]
    print solution.eventualSafeNodes(graph)
