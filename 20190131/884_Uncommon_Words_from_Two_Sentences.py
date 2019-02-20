"""
File: 884_Uncommon_Words_from_Two_Sentences.py
Date: 2019/02/20 21:07:13
"""
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        counter = collections.defaultdict(int)
        for item in A.split(' ') + B.split(' '):
            counter[item] += 1
        return [k for k in counter if counter[k] == 1]        
