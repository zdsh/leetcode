"""
File: 705_Design_HashSet.py
Date: 2019/03/18 11:28:52
"""
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.itemsPerBucket = 1001
        self.table = [[] for _ in range(self.buckets)]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if not self.contains(key):
            hashKey = key % self.buckets
            if len(self.table[hashKey]) <= 0:
                self.table[hashKey] = [False] * self.itemsPerBucket
            self.table[hashKey][key/self.buckets] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            hashKey = key % self.buckets
            self.table[hashKey][key/self.buckets] = False

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        hashKey = key % self.buckets
        if len(self.table[hashKey]) <= 0:
            return False
        return self.table[hashKey][key/self.buckets]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
