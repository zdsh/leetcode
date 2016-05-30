class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if len(preorder)==0:
            return False
        if len(preorder)==1 and preorder=='#':
            return True
        stack=[]
        stack_state=[]
        words=preorder.split(',')
        size=len(words)
        for i in range(0,size):
            p=words[i]
            if p!='#':
                stack.append(p)
                stack_state.append(0)
            else:
                if len(stack)<=0:
                    return False
                if stack_state[-1]==0:
                    stack_state[-1]=1
                else:
                    while len(stack)>0 and stack_state[-1]==1:
                        stack.pop()
                        stack_state.pop()
                    if len(stack)>0 and stack_state[-1]==0:
                        stack_state[-1]=1
                    else:
                        if i!=size-1:
                            return False
        if len(stack)==0:
            return True
        else:
            return False
