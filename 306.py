class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        size=len(num)
        for i in range(1,size-1):
            if i>1 and num[0]=='0':
                break
            j=i+1
            while j<size:
                val1=num[0:i]
                val2=num[i:j]
                if j>i+1 and num[i]=='0':
                    break
                k=j
                while k<size:
                    val=int(val1)+int(val2)
                    s=len(str(val))
                    if str(val)==num[k:k+s]:
                        k+=s
                        val1,val2=val2,val
                    else:
                        break
                if k==size:
                    return True
                j+=1
        return False
                
