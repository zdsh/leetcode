class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        visited = {}
        ret = 0
        for x in range(0, m):
            for y in range(0, n):
                if grid[x][y] == 0 or (x, y) in visited:
                    continue
                visited[(x, y)] = 1
                seq, safe, num = [(x, y)], False, 0
                while seq:
                    x_, y_ = seq.pop()
                    num += 1
                    if x_ == 0 or x_ == m-1 or y_ == 0 or y_ == n-1:
                        safe = True
                    for (xx, yy) in [(-1,0), (1,0), (0,-1), (0, 1)]:
                        if x_+xx < 0 or x_+xx >= m or y_+yy < 0 or y_+yy >= n :
                            continue
                        if grid[x_+xx][y_+yy] != 1 or (x_+xx, y_+yy) in visited:
                            continue
                        seq.append((x_+xx, y_+yy))
                        visited[(x_+xx, y_+yy)] = 1
                        
                if not safe:
                    ret += num
        return ret        
