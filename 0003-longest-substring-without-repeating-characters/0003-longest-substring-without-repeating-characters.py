class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        max_length = 0
        for l in s:
            if l not in sub:
                sub += l
                max_length =max(len(sub), max_length)
            else:
                if sub[-1] == l or sub[0] != l:
                    max_length =max(len(sub), max_length)
                    sub = l
                else:
                    max_length =max(len(sub), max_length)
                    sub = sub[1:] + l
        return max_length

                    