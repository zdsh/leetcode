class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    continue
                q = [(i,j)]
                grid[i][j] = 2
                is_island = True
                while q:
                    x, y = q.pop()
                    if x == 0 or x == m-1 or y == 0 or y == n-1:
                         is_island = False
                    for xx, yy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        if x + xx >= 0 and x+xx < m and y+yy >= 0 and y+yy < n and grid[x+xx][y+yy] == 0:
                            q += [(x+xx, y+yy)]
                            grid[x+xx][y+yy] = 2
                if is_island:
                    ret += 1
        return ret
