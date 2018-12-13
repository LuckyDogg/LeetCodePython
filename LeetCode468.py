import re

class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        pattern = re.compile(r'^[1-2]\d{0,2}.^[1-2]\d{0,2}.^[1-2]\d{0,2}.^[1-2]\d{0,2}')
        pattern1 = re.compile(r'[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-zA-Z]{1,4}:[0-9a-zA-Z]{1,4}')
        if pattern.search(IP):
            return "IPv4"
        elif pattern1.search(IP):
            return "IPv6"
        else:
            return "Neither"

