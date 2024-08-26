import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''
        if len(s) == 0:
            return True

        for char in s:
            if char in punc:
                s = s.replace(char, "")
        
        s = s.lower().replace(" ","")
        start = 0
        end = len(s)-1
        while start < end:
            if s[start] != s[end]:
                return False
            else:
                start +=1
                end -=1
        return True

        