"""
File: 803_Bricks_Falling_When_Hit.py
Date: 2019/03/11 11:32:53
"""
class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        def check(grid, x, y):
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[x]) and grid[x][y] == 1:
                return True
            return False

        def dfs(grid, r, c, left_gird):
            left_gird[r][c] = 1
            ret = 1
            for x, y in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
                if check(grid, x, y) and left_grid[x][y] == 0:
                    ret += dfs(grid, x, y, left_gird)
            return ret

        ret = []
        for hit in hits:
            r, c = hit[0], hit[1]
            grid[r][c] -= 1

        left_grid = [[0 for c in range(len(grid[r]))] for r in range(len(grid))]
        for i in range(len(grid[0])):
            if check(grid, 0, i):
                dfs(grid, 0, i, left_grid)
        for hit in hits[::-1]:
            r, c = hit[0], hit[1]
            grid[r][c] += 1
            n2 = 0
            if check(grid, r, c):
                if r == 0:
                    n2 = dfs(grid, r, c, left_grid)
                else:
                    for x, y in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
                        if check(grid, x, y) and left_grid[x][y] == 1:
                            n2 = dfs(grid, r, c, left_grid)
                            break
            ret.append(n2 - 1 if n2 > 0 else 0)
        return ret[::-1]

if __name__ == '__main__':
    solution = Solution()
    grid = [[1,0,0,0],[1,1,1,0]]
    hits = [[1,0]]
#grid = [[1,0,0,0],[1,1,0,0]]
#    hits = [[1,1],[1,0]]
#grid = [[1],[1],[1],[1],[1]]
#    hits = [[3,0],[4,0],[1,0],[2,0],[0,0]]
    grid = [[1,1,1,0,1,1,1,1],[1,0,0,0,0,1,1,1],[1,1,1,0,0,0,1,1],[1,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0]]
    hits = [[4,6],[3,0],[2,3],[2,6],[4,1],[5,2],[2,1]]
    print solution.hitBricks(grid, hits)
