class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        ret, dis, que =0, {}, []
        for x in range(0, m):
            for y in range(0, n):
                if grid[x][y] == 1:
                    que.append((x,y))
                    dis[(x,y)] = 1
        
        while que:
            (x,y) = que.pop(0)
            for xx, yy in [(x-1, y), (x, y-1), (x, y+1), (x+1, y)]:
                if xx < 0 or xx >= m or yy < 0 or yy >= n or (xx,yy) in dis:
                    continue
                dis[(xx,yy)] = dis[(x,y)] + 1
                ret = max(dis[(xx,yy)], ret)
                que.append((xx,yy))
        return ret - 1
