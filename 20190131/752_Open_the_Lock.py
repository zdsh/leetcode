"""
File: 752_Open_the_Lock.py
Date: 2019/03/21 11:08:02
"""
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        ret, initial, visited = -1, '0000', {}
        deadends = set(deadends)
        if initial in deadends:
            return -1
        queue = collections.deque()
        queue.append((initial, 0))
        visited[initial] = True
        while queue:
            cur, step = queue.popleft()
            if cur == target:
                return step
            for i, v in enumerate(cur):
                newstate = cur[0:i] + str((int(cur[i])+9)%10) + cur[i+1:]
                if newstate not in deadends and newstate not in visited:
                    queue.append((newstate, step+1))
                    visited[newstate] = True
                newstate = cur[0:i] + str((int(cur[i])+1)%10) + cur[i+1:]
                if newstate not in deadends and newstate not in visited:
                    queue.append((newstate, step+1))
                    visited[newstate] = True
        return -1  
