class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if len(b)==0:
            return 1
        if len(b)==1:
            i,value,s=0,int(b[-1]),1
            while i<value:
                s=(s*a)%1337
                i+=1
            return s
        f=self.superPow(a,b[0:len(b)-1]) 
        e=self.superPow(a,b[len(b)-1:])
        s=1
        for i in range(0,10):
            s=(s*f)%1337
        t= (s*e)%1337
        return t
            
