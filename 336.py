class Solution(object):
    def isPalindrome(self,word):
        size=len(word)
        for i in range(0,size/2):
            if word[i]!=word[size-1-i]:
                return False
        return True
        
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ret_val=[]
        map_words={y:x for x,y in enumerate(words)}
        for id,word in enumerate(words):
            if '' in map_words and word!='' and self.isPalindrome(word):
                id_null=map_words['']
                ret_val.append([id_null,id])
                ret_val.append([id,id_null])

            r_word=word[::-1]
            if r_word in map_words and map_words[r_word]!=id:
                id_r=map_words[r_word]
                ret_val.append([id,id_r])

            for i in range(1,len(word)):
                left,right=word[:i],word[i:]
                rleft,rright=left[::-1],right[::-1]
                if rright in map_words and self.isPalindrome(left):
                    id_rright=map_words[rright]
                    ret_val.append([id_rright,id])
                if rleft in map_words and self.isPalindrome(right):
                    id_rleft=map_words[rleft]
                    ret_val.append([id,id_rleft])
            
        return ret_val

