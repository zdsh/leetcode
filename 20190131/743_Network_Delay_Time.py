"""
File: 743_Network_Delay_Time.py
Date: 2019/04/03 11:14:25
"""
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        edges = {}
        for time in times:
            if time[0] not in edges:
                edges[time[0]] = []
            edges[time[0]].append(time[1:])

        distance, mixNodes = [float('inf')] * N, set()
        distance[K-1] = 0
        mixNodes.add(K)
        newsou = K
        while True:
            if newsou in edges:
                for edge in edges[newsou]:
                    v = distance[newsou-1] + edge[1]
                    if v < distance[edge[0]-1]:
                        distance[edge[0]-1] = v
            minDis, newsou = float('inf'), -1
            for i in range(N):
                if i+1 not in mixNodes:
                    if distance[i] < minDis:
                        newsou, minDis = i+1, distance[i]
            if newsou == -1:
                break
            mixNodes.add(newsou)
        return max(distance) if max(distance) != float('inf') else -1        
