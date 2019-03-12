"""
File: 797_All_Paths_From_Source_to_Target.py
Date: 2019/03/12 16:31:10
"""
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        ret, que = [], collections.deque()
        for v in graph[0]:
            if v == len(graph) - 1:
                ret.append([0, v])
            else:
                que.append([0, v])
        while que:
            path = que.popleft()
            for v in graph[path[-1]]:
                if v == len(graph) - 1:
                    ret.append(path + [v])
                else:
                    que.append(path + [v])
        return ret 
