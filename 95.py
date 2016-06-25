#Solution for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def copy_tree(root):
            if root==None:
                return None
            new_root=TreeNode(root.val)
            new_root.left=copy_tree(root.left)
            new_root.right=copy_tree(root.right)
            return new_root
            
        res=[[] for _ in range(0,n+1)]
        if n<=0:
            return []
        res[1]=[TreeNode(1)]
        for i in range(2,n+1):
            for tree in res[i-1]:
                root=tree
                p,pre,d=root.right,root,1
                while p!=None:
                    new_root=copy_tree(root)
                    new_node=TreeNode(i)
                    new_pre=new_root
                    for j in range(1,d):
                        new_pre=new_pre.right
                    new_node.left=new_pre.right
                    new_pre.right=new_node
                    res[i].append(new_root)
                    pre=p
                    p=p.right
                    d+=1

                new_root=copy_tree(root)
                new_node=TreeNode(i)
                new_node.left=new_root
                res[i].append(new_node)
                
                new_root=copy_tree(root)
                p,pre=new_root.right,new_root
                while p!=None:
                    pre=p
                    p=p.right
                new_node=TreeNode(i)
                pre.right=new_node
                res[i].append(new_root)
        return res[n]
                
            
