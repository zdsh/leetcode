#Solution for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head==None:
            return None
        if head.next==None:
            return TreeNode(head.val)
        p=head
        q=p
        while q!=None:
            q=q.next
            if q!=None:
                q=q.next
                pre=p
                p=p.next

        pre.next=None
        root=TreeNode(p.val)
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(p.next)
        return root
