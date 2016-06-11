class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.ret=[]
        self.target=target
        for i in range(1,len(num)+1):
            val=num[:i]
            if i==1 or (i>1 and num[0] !='0'):
                self.dfs(num[i:],val,int(val),int(val))
        return self.ret
        
    def dfs(self,num,res,cur,last):
        if len(num)==0:
            if cur==self.target:
                self.ret.append(res)
            return
        
        for i in range(1,len(num)+1):
            val=num[:i]
            if i==1 or (i>1 and num[0] !='0'):
                self.dfs(num[i:],res+'+'+val,cur+int(val),int(val))
                self.dfs(num[i:],res+'-'+val,cur-int(val),-int(val))
                self.dfs(num[i:],res+'*'+val,cur-last+last*int(val),last*int(val))
