"""
File: 792_Number_of_Matching_Subsequences.py
Date: 2019/03/14 11:20:47
"""
class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        import bisect
        word_dic, ret  = {}, 0
        for i, w in enumerate(S):
            if w not in word_dic:
                word_dic[w] = []
            word_dic[w].append(i)
        for word in words:
            p = -1
            for w in word:
                if w not in word_dic:
                    p = -1
                    break
                else:
                    q = bisect.bisect(word_dic[w], p)
                    if q >= len(word_dic[w]):
                        p = -1
                        break
                    else:
                        p = word_dic[w][q]
           
            if p != -1:
                ret += 1
        return ret

if __name__ == '__main__':
    sol = Solution()
    S = "abcde"
    words = ["a","bb","acd","ace"]
    print sol.numMatchingSubseq(S, words)
