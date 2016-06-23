# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None:
            return head
        n=0
        p,e=head,None
        while p!=None:
            n+=1
            e=p
            p=p.next
        k=k%n
        if k==0:
            return head
        pre,p=None,head
        i=0
        while i<n-k-1:
            i+=1
            p=p.next
        q=p.next
        p.next=None
        e.next=head
        return q
        
        
