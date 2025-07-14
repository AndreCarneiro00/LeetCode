class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            for i, num in enumerate(nums):
                if num > target:
                   return nums.index(num)
                if i == len(nums) - 1:
                    return nums.index(num) + 1
        
        return nums.index(target)