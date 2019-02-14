"""
File: 929_Unique_Email_Addresses.py
Date: 2019/02/14 11:48:26
"""
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        ret = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = local_name.split('+')[0].replace('.', '')
            ret.add(local_name + domain_name)
        return len(ret)        
