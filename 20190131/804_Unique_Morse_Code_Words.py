"""
File: 804_Unique_Morse_Code_Words.py
Date: 2019/03/01 11:47:27
"""
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ret = set()
        for word in words:
            morse_word = [morse[ord(w) - ord('a')] for w in word] 
            ret.add(''.join(morse_word))
        return len(ret)
