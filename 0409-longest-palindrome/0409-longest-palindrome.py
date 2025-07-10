class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_set = set()
        n = 0

        for char in s:
            if char in char_set:
                char_set.remove(char)
                n += 2
            else:
                char_set.add(char)
        
        if char_set:
            n +=1
        return n
        
