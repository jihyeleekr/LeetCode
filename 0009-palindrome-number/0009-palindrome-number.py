class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        res = [int(l) for l in str(x)]
        i, j = 0, len(res) -1
        
        while i < j:
            if res[i] != res[j]:
                return False
            i += 1
            j -= 1
        return True

        