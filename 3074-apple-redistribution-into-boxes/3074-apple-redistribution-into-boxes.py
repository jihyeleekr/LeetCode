class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        capacity.sort()
        capacity = list(reversed(capacity))
        cnt = 0
        cap = 0
        total_apple = sum(apple)
        for capa in capacity:
            if cap < total_apple:
                cap += capa
                cnt+=1
            else:
                break
        return cnt
        