class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        opt = 0

        for num in set(nums):
            if nums.count(num) > 1:
                opt = self.minimumOperations(nums[3::]) + 1
                break
        return opt 

        