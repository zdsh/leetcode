"""
File: 710_Random_Pick_with_Blacklist.py
Date: 2019/03/19 16:38:08
"""
class Solution(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.blackMap = {}
        self.N, top = N - 1 - len(blacklist), N - 1
        for v in blacklist:
            self.blackMap[v] = v
        for i, v in enumerate(blacklist):
            if v > self.N:
                continue
            while top in self.blackMap:
                top -= 1
            self.blackMap[v] = top
            top -= 1

    def pick(self):
        """
        :rtype: int
        """
        v = random.randint(0, self.N)
        return v if v not in self.blackMap else self.blackMap[v]

# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
