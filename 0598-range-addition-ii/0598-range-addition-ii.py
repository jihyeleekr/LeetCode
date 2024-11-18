import math
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return m * n
        else:
            ops_s = []
            [ops_s.append(x) for x in ops if x not in ops_s]
            ops_s.sort()
            ai = min(ops_s)[0]
            bi = math.inf
            for i in range(len(ops_s)):
                if bi > ops_s[i][1]:
                    bi = ops_s[i][1]
            return ai * bi
        