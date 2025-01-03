class Solution:
    def hammingWeight(self, n: int) -> int:
        bit = []
        while n != 0:
            bit.append(n % 2)
            n = n // 2
        return bit.count(1)
        