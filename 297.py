#Definition for a binary tree node.dddd
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        seq=[]
        seq.append(root)
        ret=[]
        while len(seq)>0:
            cur=seq[0]
            del seq[0]
            if cur!=None:
                seq.append(cur.left)
                seq.append(cur.right)
                ret.append(str(cur.val))
            else:
                ret.append('null')
        while len(ret)>0 and ret[-1]=='null':
            del ret[-1]
        return '['+','.join(ret)+']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        root=None
        if data=='[]':
            return root
        items=data[1:len(data)-1].split(',')
        n=len(items)
        nodes=[None]*n
        for i in range(n):
            if items[i]!='null':
                node=TreeNode(int(items[i]))
                nodes[i]=node
        
        i=0
        null_num=0
        while 2*(i-null_num)+1<n:
            if nodes[i]!=None:
                nodes[i].left=nodes[2*(i-null_num)+1]
                if 2*(i-null_num)+2<n:
                    nodes[i].right=nodes[2*(i-null_num)+2]
            else:
                null_num+=1
            i+=1
        root=nodes[0]
        return root
    

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
