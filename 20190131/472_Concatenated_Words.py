"""
File: 472_Concatenated_Words.py
Date: 2019/02/03 13:37:16
"""

class Solution(object):
    def check(self, words, word, position):
        if position == len(word):
            return 0
        for i in range(position + 1, len(word) + 1):
            if word[position : i] in words:
                num = self.check(words, word, i) 
                if num >= 0:
                    return num + 1
        return -1

    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        for word in words:
            print self.check(words, word, 0) 
            if self.check(words, word, 0) > 1:
                ans.append(word)
        return ans 

if __name__ == '__main__':
    solution = Solution()
    words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    print solution.findAllConcatenatedWordsInADict(words)
