"""
File: 706_Design_HashMap.py
Date: 2019/03/18 12:46:22
"""
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.itemsPerBucket = 1001
        self.table = [[] for _ in range(self.buckets)]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        hashKey = key % self.buckets
        if len(self.table[hashKey]) <= 0:
            self.table[hashKey] = [None] * self.itemsPerBucket
        self.table[hashKey][key/self.buckets] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hashKey = key % self.buckets
        if len(self.table[hashKey]) <= 0 or self.table[hashKey][key/self.buckets] == None:
            return -1
        return self.table[hashKey][key/self.buckets]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        hashKey = key % self.buckets
        if len(self.table[hashKey]) > 0 and self.table[hashKey][key/self.buckets] != None:
            self.table[hashKey][key/self.buckets] = None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
