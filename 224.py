class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret=0
        sig=1
        rec=[]
        i=0
        while i<len(s):
            if s[i].isdigit():
                j=i+1
                while j<len(s) and s[j].isdigit():
                    j+=1
                if sig==1:
                    ret+=int(s[i:j])
                else:
                    ret+=-int(s[i:j])
                i=j
            elif s[i]=='(':
                rec.append(ret)
                rec.append(sig)
                ret=0
                sig=1
                i+=1
            elif s[i]==')':
                a=rec[-1]*ret
                del rec[-1]
                ret=rec[-1]+a
                del rec[-1]
                i+=1
            elif s[i]=='+':
                sig=1
                i=i+1
            elif s[i]=='-':
                sig=-1
                i=i+1
            elif s[i]==' ':
                i=i+1
        return ret

