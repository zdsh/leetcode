"""
File: 936_Stamping_The_Sequence.py
Date: 2019/02/17 15:40:01
"""
class Solution(object):
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        if len(set(stamp)) < len(set(target)):
            return []

        def compareStr(stamp, target):
            n = len(stamp)
            for i in xrange(n):
                if stamp[i] != target[i] and target[i] != ' ':
                    return False
            return True

        m = len(stamp)
        n, ret = 0, []
        queue = collections.deque()
        queue.append((str(target), 0))
        while queue:
            
            cur_target, p = queue.popleft()
            if len(cur_target) < m and n >= 10 * len(target):
                return []
            if len(cur_target) == m:
                if compareStr(stamp, cur_target):
                    n += 1
                    if cur_target[0:] != ' ' * m:
                        ret.append(p + 0)
                    continue
                else:
                    return []

            valid = False
            for i in range(0, len(cur_target) - m + 1):
                if compareStr(stamp, cur_target[i:i+m]):
                    valid = True
                    n += 1
                    if cur_target[i:i+m] != ' ' * m:
                        ret.append(p + i)
                    if i > 0:
                        queue.append((cur_target[0:i] + ' ' * (m - 1), p))
                    if i + m < len(cur_target):
                        queue.append((' ' * (m - 1) + cur_target[i + m:], p + i + 1))
                    break
            if not valid:
                return []
        return ret[::-1]
