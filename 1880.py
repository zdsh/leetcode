class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        def convertNum(word):
            return int(''.join([str(ord(w) - ord('a')) for w in word]))
        firstNum = convertNum(firstWord)
        secondNum = convertNum(secondWord)
        return  firstNum + secondNum == convertNum(targetWord)

a = Solution()
a.isSumEqual('acb', 'cba', 'cdb')
