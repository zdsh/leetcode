"""
File: 756_Pyramid_Transition_Matrix.py
Date: 2019/02/26 16:24:45
"""
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        n = len(bottom)
        mapped = {}
        for a in allowed:
            if a[0:2] not in mapped:
                mapped[a[0:2]] = set()
            mapped[a[0:2]].add(a[2])
        while n >= 2:
            top = [set()] * (n - 1)
            for k in range(0, n - 1):
                pairs = [l + r for l in bottom[k] for r in bottom[k+1]]
                for p in pairs:
                    if p in mapped:
                        top[k] = top[k].union((mapped[p]))
            for block in top:
                if len(block) <= 0:
                    return False
            bottom = top
            n -= 1
        return True  
