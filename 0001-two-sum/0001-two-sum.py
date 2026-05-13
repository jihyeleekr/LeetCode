class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d_map ={}

        for i, val in enumerate(nums):
            comp = target - val

            if comp in d_map:
                return [d_map[comp], i]
            d_map[val] = i
    
