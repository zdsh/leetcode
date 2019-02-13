"""
File: 911_Online_Election.py
Date: 2019/02/12 11:58:00
"""
class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.leads = []
        count ={}
        self.times = times
        lead = -1
        for t, p in zip(times, persons):
            count[p] = count.get(p, 0) + 1
            if count[p] >= count.get(lead, 0):
                lead = p
            self.leads.append(p)

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        ret = self.leads[bisect.bisect(self.times, t) - 1]
        return ret
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

