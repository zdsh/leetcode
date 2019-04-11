"""
File: 722_Remove_Comments.py
Date: 2019/03/20 11:25:10
"""
class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        ret, notBlock = [], True
        for line in source:
            j = 0
            if notBlock:
                newline = ''
            while j < len(line):
                if notBlock and line[j:j+2] == '//':
                    break
                elif notBlock and line[j:j+2] == '/*':
                    notBlock = False
                    j += 1
                elif notBlock == False and line[j:j+2] == '*/':
                    notBlock = True
                    j += 1
                elif notBlock:
                    newline += line[j]
                j += 1
                
            if newline != '' and notBlock:
                ret.append(newline)
        return ret
