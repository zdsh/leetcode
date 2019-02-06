# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        res_dic = {}
        def travel(r, x, y, res_dic):
            if x not in res_dic:
                res_dic[x] = {}
            if y not in res_dic[x]:
                res_dic[x][y] = []
            res_dic[x][y].append(r.val)
            if r.left != None:
                travel(r.left, x - 1, y - 1, res_dic)
            if r.right != None:
                travel(r.right, x + 1, y - 1, res_dic)
        travel(root, 0, 0, res_dic)
        ret = []
        
        for x in sorted(res_dic):
            y_dic = res_dic[x]
            v = []
            for y in sorted(y_dic, reverse=True):
                v += sorted(y_dic[y])
            ret.append(v)
        return ret

