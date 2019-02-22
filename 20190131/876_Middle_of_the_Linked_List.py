"""
File: 876_Middle_of_the_Linked_List.py
Date: 2019/02/22 21:30:30
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1 = head
        p2 = head
        while True:
             if p2.next != None:
                 if p2.next.next != None:
                      p2 = p2.next.next
                      p1 = p1.next
                 else:
                      return p1.next
             else:
                 return p1
