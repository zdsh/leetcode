class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        diff = [(a, b) for a, b in zip(A, B) if a != b]
        if len(diff) == 0 and len(set(A)) < len(A):
            return True
        elif len(diff) == 2 and diff[0][0] == diff[1][1] and diff[1][0] == diff[0][1]:
            return True
        else:
            return False

