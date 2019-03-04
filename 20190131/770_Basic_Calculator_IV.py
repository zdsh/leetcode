"""
File: 770_Basic_Calculator_IV.py
Date: 2019/03/04 16:55:10
"""
import collections
class Solution(object):
    def basicCalculatorIV(self, expression, evalvars, evalints):
        """
        :type expression: str
        :type evalvars: List[str]
        :type evalints: List[int]
        :rtype: List[str]
        """
        var_dic = dict(zip(evalvars, evalints))
        expression = expression.replace(' ', '')
        stack = []
        i, s = 0, 0
        while i < len(expression):
            e = expression[i]
            if e == '(':
                j, c = i + 1, 1
                while True:
                    if expression[j] == '(':
                        c += 1
                    if expression[j] == ')':
                        c -= 1
                    print expression[j:], c, j
                    if c == 0:
                        print 'c==0', expression[i+1:j]
                        break
                    j += 1
                print i+1, j, expression[i+1:j]
                res = self.basicCalculatorIV(expression[i+1:j], evalvars, evalints)
                stack.append(res)
                i = j + 1
                s = i
            elif e in ['-', '+', '*']:
                if s != i:
                    print expression[s:i] in var_dic
                    if expression[s:i] in var_dic:
                        stack.append([str(var_dic[expression[s:i]])])
                    else:
                        stack.append([expression[s:i]])
                    
                stack.append(e)
                i += 1
                s = i
            else:
                i += 1
        if s != len(expression):
            stack.append([str(var_dic[expression[s:]]) if expression[s:] in var_dic else expression[s:]])
        print expression, stack

        for i in range(1, len(stack) - 1, 2):
            if stack[i] == '*': 
                stack[i+1] = [s1 + '*' + s2 for s1 in stack[i-1] for s2 in stack[i+1]] 
                stack[i-1] = '*'
                if i >= 2 and stack[i-2] == '-':
                    stack[i] = '-'
        print stack
        ret = collections.defaultdict(int)
        for i in range(0, len(stack), 2):
            if stack[i] != '*':
                for j in range(0, len(stack[i])):
                    items = stack[i][j].split('*') 
                    print items
                    coffi_items = [int(v) for v in items if not v.isalpha()]
                    coffi = reduce(lambda x,y:x*y, coffi_items) if len(coffi_items) > 0 else 1
                    letters = sorted([v for v in items if v.isalpha()])
                    if i > 0 and stack[i-1] == '-':
                        coffi = -coffi
                    ret['*'.join(letters)] += coffi
        r = []
        for k in sorted(ret, key=lambda x:(-len([i for i in x.split('*') if i.isalpha()]), [i for i in x.split('*') if i.isalpha()])):
            v = '*'.join([str(ret[k]), k]) if k != '' else str(ret[k])
            if ret[k] != 0:
                r.append(v)
        print '----'
        return r 
if __name__ == '__main__':
    solution = Solution()
    evalvars = ["e"]
    evalints = [1]
    expression = "e + 8 - a + 5" 
    print solution.basicCalculatorIV(expression, evalvars, evalints) 
    expression = "e - 8 + temperature - pressure"
    evalvars = ["e", "temperature"]
    evalints = [1, 12]
    print solution.basicCalculatorIV(expression, evalvars, evalints) 
    expression = "(e + 8) * (e - 8)"
    evalvars = [] 
    evalints = []
    print solution.basicCalculatorIV(expression, evalvars, evalints) 
    expression = "7 - 7"
    evalvars = []
    evalints = []
    print solution.basicCalculatorIV(expression, evalvars, evalints) 
    expression = "a * b * c + b * a * c * 4"
    evalvars = []
    evalints = []
    print solution.basicCalculatorIV(expression, evalvars, evalints) 
    expression = "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))"
    evalvars = []
    evalints = []
    expression = "a"
    evalvars = ['a']
    evalints = [13]
    print solution.basicCalculatorIV(expression, evalvars, evalints) 
    expression = "a * b - b * a"
    evalvars = []
    evalints = []
    print solution.basicCalculatorIV(expression, evalvars, evalints) 
    expression = "(av * 9) - (ar + 0) - ((bq - cv) + v * (b + bq - bk)) * (a - 12 + 2 - (6 * cc - 8 - bv + ag))"
    evalvars = ["d", "g", "h", "j", "l", "o", "s", "u", "v", "w", "af", "ag", "ah", "ak", "at", "au", "av", "aw", "az", "bc", "be", "bg", "bj", "bm", "bn", "bq", "br", "bs", "bt", "bu", "bv", "bw", "bx", "by", "bz", "ca", "cd", "ce", "cf", "ch", "ci", "ck", "cq", "cr", "cs", "cu", "cv"]
    evalints = [3, 6, 7, 9, 11, 1, 5, 7, 8, 9, 10, 11, 12, 2, 11, 12, 0, 1, 4, 12, 1, 3, 6, 9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 5, 6, 7, 9, 10, 12, 5, 6, 7, 9, 10]
    print solution.basicCalculatorIV(expression, evalvars, evalints) 
