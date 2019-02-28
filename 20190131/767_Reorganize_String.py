"""
File: Reorganize_String.py
Date: 2019/02/27 20:59:25
"""
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        couons.Counter(S)

        ret = ''
        while counter:
            stop = True
            for s, c in counter.most_common():
                if len(s) == 0 or ret[-1] != s:
                    ret += s
                    counter[s] -= 1
                    if not counter[s]:
                        del counter[s]
                    stop = False
                    break
            if stop:
                retur ''
        return ret
