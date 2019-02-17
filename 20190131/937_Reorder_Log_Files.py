"""
File: 937_Reorder_Log_Files.py
Date: 2019/02/17 11:14:33
"""
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        ret = []
        log_digit = []
        log_letter_dic = {}
        for index, log in enumerate(logs):
            items = log.split(' ')
            if items[1].isdigit():
                log_digit.append(log)
            else:
                log_letter_dic[' '.join(items[1:])] = index
        
        for v in sorted(log_letter_dic.items(), key=lambda v:v[0]):
            ret.append(logs[v[1]])
        ret += log_digit
        return ret     
