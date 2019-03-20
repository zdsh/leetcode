"""
File: 726_Number_of_Atoms.py
Date: 2019/03/20 14:11:14
"""
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        import collections
        def getAtom(s, i):
            j = i + 1
            while j < len(s) and s[j].isalpha() and s[j].lower() == s[j]:
                j += 1
            atom = s[i:j]
            k = j
            while k < len(s) and s[k].isdigit():
                k += 1
            coff = 1 if s[j:k] == '' else int(s[j:k]) 
            return (atom, coff, k)

        res = collections.defaultdict(int)
        i, n = 0, len(formula)
        while i < n:
            v = formula[i]
            if v.isalpha() and v.upper() == v:
                atom, coff, k = getAtom(formula, i)
                res[atom] += coff
                i = k
            elif v == '(':
                n_l = 1
                j = i + 1
                while j < n:
                    n_l += 1 if formula[j] == '(' else 0
                    n_l -= 1 if formula[j] == ')' else 0
                    if n_l == 0:
                        break
                    j += 1
                subret = self.countOfAtoms(formula[i+1:j])
                k = j + 1
                while k < n and formula[k].isdigit():
                    k += 1
                coff = 1 if formula[j+1:k] == '' else int(formula[j+1:k]) 
                t = 0
                while t < len(subret):
                    atom, c, p = getAtom(subret, t)
                    res[atom] += c * coff
                    t = p
                i = k

        return ''.join([k + str(res[k]) if res[k] > 1 else k for k in sorted(res.keys())])

if __name__ == '__main__':
    sol = Solution()
    formula = "K4(ON(SO3)2)2"
    formula = "((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14"
    print sol.countOfAtoms(formula)
