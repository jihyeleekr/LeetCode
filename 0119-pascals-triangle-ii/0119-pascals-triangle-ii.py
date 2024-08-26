class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = self.generate(rowIndex+1)
        return result[rowIndex]
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1,1]]
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            result = [[1]] + result
            return result
        else:
            self.pascal(numRows-2, result)
            result = [[1]] + result
        return result
    def pascal(self, n, result):
        row_list = [1]
        if n == 0:
            return result
        else:
            sublist = result[-1]
            for j in range(len(sublist)-1):
                row_list.append(sublist[j]+sublist[j+1])
            row_list.append(1)
            result.append(row_list)
            n -= 1
        return self.pascal(n, result)