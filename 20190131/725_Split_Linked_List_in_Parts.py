"""
File: 725_Split_Linked_List_in_Parts.py
Date: 2019/03/20 11:48:40
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        ph = root
        ret = []
        while ph != None:
            ret.append(ph)
            pk  = ph
            while ph != None and pk != None:
                i = 0
                while i < k and pk != None:
                    i += 1
                    pk = pk.next
                if pk != None:
                    ph = ph.next
            pn = ph.next
            ph.next = None
            ph = pn
            k -= 1
        for i in range(k):
            ret.append([])
        return ret        
