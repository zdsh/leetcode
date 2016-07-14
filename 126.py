class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        def getpaths(pre,word):
            #print 'getpahts',pre,word
            if len(pre[word])<=0:
                return [[word]]
            pre_word_list=pre[word]
            paths=[]
            for pre_word in pre_word_list:
                paths=paths+getpaths(pre,pre_word)
            for path in paths:
                path.append(word)
            #print ("get paths end",pre,word,paths)
            return paths
                
        ret=[]
        if beginWord==endWord:
            return [beginWord]
        seq=[]
        seq.append(beginWord)
        pace,pre={},{}
        min_pace=len(wordlist)+10
        pace[beginWord]=0
        pre[beginWord]=[]
        word_set=set(wordlist)
        while len(seq)>0:
            #print 'seq',seq
            word=seq[0]
            if pace[word]>=min_pace:
                break
            for i in range(0,len(word)):
                for l in 'abcdefghijklmnopqrstuvwxyz':
                    new_word=word[0:i]+l+word[i+1:]
                    if new_word==endWord:
                        min_pace=pace[word]+1
                        paths=getpaths(pre,word)
                        for path in paths:
                            ret.append(path[::]+[new_word])
                        #print ret
                    elif new_word in pre:
                        if pace[word]>=pace[new_word]:
                            continue
                        pre[new_word].append(word)

                    elif new_word in word_set:
                        pace[new_word]=pace[word]+1
                        pre[new_word]=[word]
                        word_set.remove(new_word)
                        seq.append(new_word)
            del seq[0]
        #print 'last ret',ret
        return ret
        
p=Solution()
print(p.findLadders('a','c',["a","b","c"]))          
print(p.findLadders('hit','cog',["hot","dot","dog","lot","log"]))          
print(p.findLadders('red','tax',["ted","tex","red","tax","tad","den","rex","pee"]))          
