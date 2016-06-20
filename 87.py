class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        size1,size2=len(s1),len(s2)
        if size1!=size2:
            return False
        if set(s1)!=set(s2):
            return False
        if s1==s2:
            return True
        if sorted(s1) != sorted(s2): return False
        l1_dic=collections.defaultdict(int)
        l2_dic=collections.defaultdict(int)
        r2_dic=collections.defaultdict(int)
        for i in range(0,size1-1):
            l1_dic[s1[i]]+=1
            l2_dic[s2[i]]+=1
            r2_dic[s2[size1-1-i]]+=1
            if l1_dic==l2_dic:
                if self.isScramble(s1[:i+1],s2[:i+1]) and self.isScramble(s1[i+1:],s2[i+1:]):
                    return True
            elif l1_dic==r2_dic:
                if self.isScramble(s1[:i+1],s2[size1-1-i:]) and self.isScramble(s1[i+1:],s2[:size1-1-i]):
                    return True                
        return False
