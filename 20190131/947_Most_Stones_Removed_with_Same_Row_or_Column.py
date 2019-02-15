"""
File: 947_Most_Stones_Removed_with_Same_Row_or_Column.py
Date: 2019/02/15 18:23:40
"""
import collections

class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        def getNeighboors(stone, stones):
            neighboors = []
            for s in stones:
                if s[0] == stone[0] or s[1] == stone[1]:
                    neighboors.append(s)
            return neighboors
        visited = {}
        ret = 0
        for stone in stones:
            if tuple(stone) in visited:
                continue
            queue = collections.deque()
            queue.append(tuple(stone))
            visited[tuple(stone)] = 1
            n = 1
            while queue:
                cur_stone = queue.popleft()
                for s in getNeighboors(cur_stone, stones):
                    if tuple(s) not in visited:
                        queue.append(tuple(s))
                        visited[tuple(s)] = 1
                        n += 1
            ret += n - 1
        return ret 
