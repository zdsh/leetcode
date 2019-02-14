"""
File: 919_Complete_Binary_Tree_Inserter.py
Date: 2019/02/13 20:52:37
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.queue = []
        q = self.root
        self.queue.append(q)
        while self.queue:
            q = self.queue[0]
            if q.left != None:
                self.queue.append(q.left)
            else:
                break
            if q.right != None:
                self.queue.append(q.right)
                del self.queue[0]
            else:
                break

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        q = self.queue[0]
        node = TreeNode(v)
        self.queue.append(node)
        if q.left == None:
            q.left = node
            return q.val
        elif q.right == None: 
            q.right = node
            del self.queue[0]
            return q.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()

