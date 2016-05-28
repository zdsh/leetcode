
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.flater_list=[]
        for n_e in nestedList:
            if n_e.isInteger():
                self.flater_list.append(n_e.getInteger())
            else:
                n_e=n_e.getList()
                sub_ni=NestedIterator(n_e)
                while sub_ni.hasNext():
                    self.flater_list.append(sub_ni.next())
        self.index=0

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            val=self.flater_list[self.index]
            self.index+=1
            return val
            
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index<len(self.flater_list):
            return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
