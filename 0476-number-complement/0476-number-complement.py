class Solution:
    def findComplement(self, num: int) -> int:
        b = ""
        while num >= 1:
            if num % 2 == 1:
                b += '0'
            else:
                b += '1'
            
            num = num // 2
        b =  b[::-1]
        n = len(b) -1
        ans = 0
        for i in range(n+1):
            if b[i] == '1':
                ans += 2 ** n
            n -=1
        return ans

        