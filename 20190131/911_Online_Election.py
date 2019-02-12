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
        self.persons = persons
        self.times = times 

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        end = len(self.times) - 1
        start = 0
        while end >= start:
            mid = (end + start) / 2
            if self.times[mid] == t:
                start = mid + 1
                break
            if self.times[mid] > t:
                end = mid - 1
            if self.times[mid] < t:
                start = mid + 1
        ret = None
        vote_dic = {}
        for i in range(0, start):
            if self.persons[i] not in vote_dic:
                vote_dic[self.persons[i]] = 0
            vote_dic[self.persons[i]] += 1
            if ret == None:
                ret = self.persons[i]
            elif vote_dic[self.persons[i]] >= vote_dic[ret]:
                ret = self.persons[i]
        return ret
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

