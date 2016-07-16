class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        s=s.replace(' ','')
        ope_stack=[]
        
        i=0
        while i<len(s) and s[i].isdigit():
            i=i+1
        value=int(s[0:i])
        ope_stack.append(value)
        
        while i<len(s):
            ope=s[i]
            i+=1
            j=i
            while i<len(s) and s[i].isdigit():
                i=i+1
            value=int(s[j:i])
            
            if ope=='*':
                ope_stack[-1]*=value
            elif ope=='/':
                ope_stack[-1]/=value
            elif ope in ['+','-']:
                ope_stack.append(ope)
                ope_stack.append(value)
        
        ret=ope_stack[0]
        if len(ope_stack)>1:
            i=1
            while i<len(ope_stack):
                if ope_stack[i]=='+':
                    ret+=ope_stack[i+1]
                elif ope_stack[i]=='-':
                    ret-=ope_stack[i+1]
                i+=2
        return ret
        
