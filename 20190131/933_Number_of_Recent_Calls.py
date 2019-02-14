"""
File: 933_Number_of_Recent_Calls.py
Date: 2019/02/14 14:06:33
"""
class RecentCounter(object):

    def __init__(self):
        self.ping_list = []
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.ping_list.append(t)
        n = bisect.bisect_left(self.ping_list, t - 3000)
        return len(self.ping_list[n:])
