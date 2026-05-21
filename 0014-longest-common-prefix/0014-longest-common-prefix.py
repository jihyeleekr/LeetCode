class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest = min(strs, key=len)

        prefix = ""

        for i in range(len(shortest)):
            pre_test = prefix + shortest[i]
            n = len(pre_test)
            for word in strs:
                if pre_test != word[:n]:
                    return prefix
            prefix += shortest[i]
        return prefix
        