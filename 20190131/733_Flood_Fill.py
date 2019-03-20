"""
File: 733_Flood_Fill.py
Date: 2019/03/20 15:36:09
"""
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        m, n = len(image), len(image[0])
        oldColor, visited = image[sr][sc], {}
        queue = collections.deque()
        queue.append((sr, sc))
        image[sr][sc] = newColor
        visited[(sr, sc)] = True
        while queue:
            r, c = queue.popleft()
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + x, c + y
                if nr >= 0 and nr < m and nc >= 0 and nc < n:
                    if image[nr][nc] == oldColor and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        image[nr][nc] = newColor
                        visited[(nr, nc)] = True
        return image      
