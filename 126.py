class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        ret=[]
        if beginWord==endWord:
            return ret[beginWord]
        seq=[]
        seq.append(beginWord)
        pace,pre={},{}
        min_pace=len(wordlist)+10
        pace[beginWord]=0
	pre[0]=None
	k=0
        while len(seq)>k:
            word=seq[k]
            k+=1
            if pace[word]>=min_pace:
                break
            for i in range(0,len(word)):
                for l in 'abcdefghijklmnopqrstuvwxyz':
                    new_word=word[0:i]+l+word[i+1:]
                    if new_word==endWord:
                        min_pace=pace[word]+1
                        path=[]
                        p=k-1
                        while pre[p]!=None:
			    print p
                            path.append(seq[p])
			    p=pre[p]
                        pa=[seq[p]]+path[::-1]+[new_word]
                        ret.append(pa)
			print('pre',pre)
			print('seq',seq)
			print('ret',pa)
                    elif new_word in wordlist:
			if new_word in pace:
			    if pace[word]>=pace[new_word]:
				continue
                        pace[new_word]=pace[word]+1
                        pre[len(seq)]=k-1
                        seq.append(new_word)
        return ret
        
p=Solution()
print(p.findLadders('a','c',["a","b","c"]))          
print(p.findLadders('hit','cog',["hot","dot","dog","lot","log"]))          
print(p.findLadders('red','tax',["ted","tex","red","tax","tad","den","rex","pee"]))          
