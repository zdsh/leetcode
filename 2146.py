class Solution(object):
    def highestRankedKItems(self, grid, pricing, start, k):
        """
        :type grid: List[List[int]]
        :type pricing: List[int]
        :type start: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        visited = {}
        que = [(0, grid[start[0]][start[1]], start[0], start[1])]
        visited[(start[0], start[1])] = 1
        ret = []
        while que:
            (dis, price, x, y) = que.pop(0)
            if price >= pricing[0] and price <= pricing[1]:
                 ret.append( (dis, price, x, y))
            for xx, yy in [(x-1, y), (x, y-1), (x, y+1), (x+1, y)]:
                if xx < 0 or xx >= m or yy < 0 or yy >= n:
                    continue
                if grid[xx][yy] == 0 or (xx, yy) in visited:
                    continue
                visited[(xx, yy)] = 1
                que.append((dis+1, grid[xx][yy], xx, yy)) 
                
        return [[x,y] for (d, p, x, y) in sorted(ret)][0:k]
