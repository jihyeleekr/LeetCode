class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return []
        rst = []
        ran = ''
        i, j = 0, 1
        while j < len(nums):
            if j - i == nums[j] - nums[i]:
                if ran == '':
                    ran = str(nums[i]) 
                else:
                    pass
            else:
                if ran == '':
                    rst.append(str(nums[i]))
                else:
                    ran += '->' + str(nums[j-1])
                    rst.append(ran)
                    ran = ''
                i = j
            j += 1
        j -=1 
        if ran != '':
            if nums[j] - nums[j-1]== 1:
                ran += '->' + str(nums[j])
                rst.append(ran)
            else:
                rst.append(ran)
                rst.append(str(nums[j]))
        else:
            rst.append(str(nums[j]))
        return rst
