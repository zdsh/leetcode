"""
File: 904_Fruit_Into_Baskets.py
Date: 2019/02/18 21:02:16
"""
class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        i = 0
        while i < len(tree) - 1 and tree[i] == tree[i + 1]:
            i += 1
        if i >= len(tree) - 1:
            return len(tree)
        pre, cur  = tree[i], tree[i + 1]
        ret = i + 2
        start = 0
        new_start = i + 1
        for k in range(i + 2, len(tree)):
            if tree[k] == pre:
                new_start = k
                pre, cur = cur, pre          
                ret = max(ret, k - start + 1)
            elif tree[k] == cur:
                ret = max(ret, k - start + 1)
            else:
                pre, cur = cur, tree[k]
                start, new_start = new_start, k
                ret = max(ret, k - start + 1)
        return ret
                 


        
