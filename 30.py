class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words)<=0:
            return []

        w=len(words[0])
        if w==0:
            return [ i for i in range(0,len(s)+1)]
       
        res=collections.defaultdict(lambda:0)
        for word in words:
            res[word]+=1
            
        i,n=0,len(words)
        ret=[]
        while i<w:
            j=i
            seen=collections.defaultdict(lambda:0)
            begin=i
            counter=n
            while j<=len(s)-counter*w:
                word=s[j:j+w]
                if  word in res:
                    seen[word]+=1
                    if seen[word]<=res[word]:
                        counter-=1
                    else:
                        while seen[word]>res[word]:
                            old_word=s[begin:begin+w]
                            if seen[old_word]<=res[old_word]:
                                counter+=1
                            seen[old_word]-=1
                            begin=begin+w
                           
                    if counter==0:
                        ret.append(begin)
                        old_word=s[begin:begin+w]
                        if seen[old_word]<=res[old_word]:
                            counter+=1
                        seen[old_word]-=1
                        begin=begin+w
                else:
                    seen=collections.defaultdict(lambda:0)
                    counter=n
                    begin=j+w
                j+=w
                    
            i+=1
        return ret
