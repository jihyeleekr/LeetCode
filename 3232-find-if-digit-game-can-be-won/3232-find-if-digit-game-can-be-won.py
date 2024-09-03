class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        for num in nums:
            if num % 10 == num:
                single += num
        return single != sum(nums) - single