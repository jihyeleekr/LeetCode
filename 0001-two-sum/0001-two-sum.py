class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = []
        for i in range(0, len(nums)):
            num = nums[i]
            for j in range(i+1,len(nums)):
                if(num + nums[j] == target):
                    index.append(i)
                    index.append(j)
        return(index)
