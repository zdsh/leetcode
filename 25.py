# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse( p, q):
            if p==q:
                return p,q
            s=p
            t=s.next
            while t!=q:
                r=t.next
                t.next=s
                s=t
                t=r
            t.next=s
            return t,p
        
        i=0
        p=head
        s=p
        pre=None
        while p!=None:
            i+=1
            q=p.next
            if i%k==0:
                b,e=reverse(s,p)
                s=q
                if pre==None:
                    head=b
                    pre=e
                else:
                    pre.next=b
                    pre=e
            p=q
        if pre==None:
            return head
        else:
            pre.next=s
        return head
            

