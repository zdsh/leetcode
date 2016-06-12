class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret=[]
        visited = set([s])    

        def calc_wrong(s):
            l,r=0,0
            for c in s:
                if c=='(':
                    l+=1
                if c==')':
                    if l>0:
                        l-=1
                    else:
                        r+=1
            return l+r
        
        def dfs(s):
            w_n=calc_wrong(s)
            if w_n==0:
                ret.append(s)
                return
            for i in range(len(s)):
                if s[i] in ['(',')']:
                    n_s=s[:i]+s[i+1:]
                    if n_s not in visited and calc_wrong(n_s)<w_n:
                        visited.add(n_s)
                        dfs(n_s)
            return

        dfs(s)
        return ret
