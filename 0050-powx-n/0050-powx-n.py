class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            rec = power(x, n // 2)
            rec *= rec

            if n % 2 == 1:
                return rec * x
            return rec
        ans = power(x, abs(n))

        if n >= 0:
            return ans
        
        return 1 / ans
