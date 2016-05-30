class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return head
        odd_head=None
        even_head=None
        even_p=None
        p=head
        i=1
        while p!=None:
            if i%2==1:
                if odd_head==None:
                    odd_head=p
                    odd_p=odd_head
                else:
                    odd_p.next=p
                    odd_p=p
            else:
                if even_head==None:
                    even_head=p
                    even_p=even_head
                else:
                    even_p.next=p
                    even_p=p
            p=p.next
            i+=1
        if even_p!=None:
            even_p.next=None
        odd_p.next=even_head
        return odd_head
