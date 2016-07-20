class TrieNode:
    def __init__(self):
        self.dic = {}
        self.end = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if self.root == None:
            self.root = TrieNode()
        node = self.root
        for w in word:
            if node.dic.get(w) == None:
                node.dic[w] = TrieNode()
            node = node.dic[w]
        node.end = 1
        
    def search(self, word):
        if self.root == None:
            return False
        node = self.root
        for w in word:
            if node.dic.get(w) == None:
                return False
            node = node.dic[w]
        if node.end == 1:
            return True
        return False
    
    def startsWith(self, prefix):
        if self.root == None:
            return False
        node = self.root
        for w in prefix:
            if node.dic.get(w) == None:
                return False
            node = node.dic[w]
        return True
        
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        tire=Trie()
        for word in words:
            tire.insert(word)
        
        ret=set()
        m=len(board)
        if m<=0:
            return []
        n=len(board[0])
        visited=[[0 for _ in range(n)] for _ in range(m)]
        
        def dfs(s,node,i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return
            if len(node.dic)<=0:
                return 
            if visited[i][j]!=0:
                return
            if board[i][j] not in node.dic:
                return
            node=node.dic[board[i][j]]
            s+=board[i][j]

            if node.end==1:
                ret.add(s)
            
            visited[i][j]=1
            dfs(s,node,i-1,j)
            dfs(s,node,i+1,j)
            dfs(s,node,i,j-1)
            dfs(s,node,i,j+1)
            visited[i][j]=0
            
        for i in range(m):
            for j in range(n):
                    dfs('',tire.root,i,j)
        return [ s for s in ret]
            
