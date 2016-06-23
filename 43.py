class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def add(num1,num2):
            num1=num1[::-1]
            num2=num2[::-1]
            size1,size2=len(num1),len(num2)
            if size1>size2:
                num1,num2=num2,num1
            ret=''
            jw=0
            for i in range(0,len(num1)):
                v=int(num1[i])+int(num2[i])+jw
                if v>=10:
                    jw=1
                    v-=10
                else:
                    jw=0
                ret+=str(v)
            for i in range(len(num1),len(num2)):
                v=int(num2[i])+jw
                if v>=10:
                    jw=1
                    v-=10
                else:
                    jw=0
                ret+=str(v)
            if jw==1:
                ret+=str(1)
            #print('ret',ret)
            return ret[::-1]
        
        tag=True
        while num2[0] in ['+','-']:
            if num2[0]=='-':
                tag=not tag
            num2=num2[1:]
        while num1[0] in ['+','-']:
            if num1[0]=='-':
                tag=not tag
            num1=num1[1:]
        ret='0'
        num2=num2[::-1]
        res={}
        res['0']='0'
        for k in range(0,len(num2)):
            if num2[k] in res:
                v=res[num2[k]]
            else:
                v='0'
                for i in range(0,int(num2[k])):
                    v=add(v,num1)
                    res[str(i+1)]=v
            for i in range(0,k):
                v+='0'
            while v[0]=='0' and len(v)>1:
                v=v[1:]
            ret=add(ret,v)
        if not tag:
            ret='-'+ret
        return ret
            
