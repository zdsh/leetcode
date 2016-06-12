class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        nums=[]
        size=len(words)
        words=sorted(words,cmp=lambda x,y:len(y)-len(x))

        for word in words:
            nums+=[sum(1<<(ord(x)-ord('a')) for x in set(word))]
        ret=0
        i=0
        while i<size and len(words[0])*len(words[i]) >ret:
            j=0
            while j<size and len(words[i])*len(words[j])>ret:
                if nums[i]&nums[j]==0:
                    ret=max(ret,len(words[i])*len(words[j]))
                j+=1
            i+=1
        return ret
