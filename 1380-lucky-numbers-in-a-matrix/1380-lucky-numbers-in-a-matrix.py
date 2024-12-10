class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        result = []
        for i in range(len(matrix)):
            k = min(matrix[i])
            k1 = matrix[i].index(k)
            m = 0
            for i2 in range(len(matrix)):
                m = max(m, matrix[i2][k1])
            
            if k == m:
                result.append(m)
        return result
    
                                         