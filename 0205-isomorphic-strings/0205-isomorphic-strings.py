class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_to_t_mapping = {}
        t_used = set()
    
        for i in range(len(s)):
            if s[i] in s_to_t_mapping:
                if s_to_t_mapping[s[i]] != t[i]:
                    return False
            else:
                if t[i] in t_used:
                    return False
                s_to_t_mapping[s[i]] = t[i]
                t_used.add(t[i])

        return True
        