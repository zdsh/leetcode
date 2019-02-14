"""
File: 934_Shortest_Bridge.py
Date: 2019/02/14 17:26:30
"""
class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        def getNeighboor(x, y, row, col):
            ret = []
            if x >= 1:
                ret.append((x-1, y))
            if x < row - 1:
                ret.append((x+1, y))
            if y >= 1:
                ret.append((x, y-1))
            if y < col - 1:
                ret.append((x, y + 1))
            return ret

        queue = collections.deque()
        row, col = len(A), len(A[0])
        visited = {}
        for i in xrange(row):
            for j in xrange(col):
                if A[i][j] == 1:
                    queue.append((i, j, 0))
                    visited[i,j] = 1
                    index = 0
                    while index < len(queue):
                        x, y, s = queue[index]
                       
                        for v in getNeighboor(x, y, row, col):
                            (xn, yn) = v
                            if (xn, yn) not in visited and A[xn][yn] == 1:
                                queue.append((xn, yn, 0))
                                visited[xn, yn] = 1
                        index += 1
                    break
            if len(queue) > 0:
                break
        
        while queue:
            x, y, s = queue.popleft()
            for (xn, yn) in getNeighboor(x, y, row, col):
                if (xn, yn) not in visited:
                    if A[xn][yn] == 1:
                        return s 
                    else:
                        queue.append((xn, yn, s + 1))
                        visited[xn, yn] = 1 
