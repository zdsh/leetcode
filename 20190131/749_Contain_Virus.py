"""
File: 749_Contain_Virus.py
Date: 2019/04/01 20:00:17
"""
class Solution(object):
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n, ret = len(grid), len(grid[0]), 0

        def dfs(grid, r, c, id, visited):
            visited[(r, c)] = id
            for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = x + r, y + c
                if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == 1 and  (nr, nc) not in visited:
                    dfs(grid, nr, nc, id, visited)

        while True:
            id, visited = -1, {}
            for r in xrange(m):
                for c in xrange(n):
                    if grid[r][c] == 1 and (r, c) not in visited:
                        virus = dfs(grid, r, c, id, visited)
                        id -= 1

            record = {}
            for r in xrange(m):
                for c in xrange(n):
                    if grid[r][c] == 1:
                        for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                            nr, nc = x + r, y + c
                            if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == 0:
                                id = visited[(r, c)]
                                if id not in record:
                                    record[id] = set()
                                record[id].add((nr, nc))
            num, choosed_id = 0, 0
            for id in record:
                if len(record[id]) > num:
                    num, choosed_id = len(record[id]), id
            if num == 0:
                return ret
            for r in xrange(m):
                for c in xrange(n):
                    if grid[r][c] == 1:
                        for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                            nr, nc = x + r, y + c
                            if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == 0:
                                if visited[(r,c)] == choosed_id:
                                    ret += 1
                        if visited[(r,c)] == choosed_id:
                            grid[r][c] = choosed_id

            for r in xrange(m):
                for c in xrange(n):
                    if grid[r][c] == 1:
                        for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                            nr, nc = x + r, y + c
                            if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == 0:
                                grid[nr][nc] = 2
            for r in xrange(m):
                for c in xrange(n):
                    if grid[r][c] == 2:
                        grid[r][c] = 1
