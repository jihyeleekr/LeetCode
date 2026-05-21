class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        hash = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        speical = {
            'IV' : 4,
            'IX' : 9,
            'XL' : 40,
            'XC' : 90,
            'CD' : 400,
            'CM' : 900
        }

        num = 0
        n = len(s)
        i = 0
        while i < n-1:
            if s[i] + s[i+1] in speical:
                num += speical[s[i] + s[i+1]]
                i += 2
            else:
                num += hash[s[i]]
                i += 1
        if i == n-1:
            num += hash[s[i]]
            return num
        else:
            return num
        