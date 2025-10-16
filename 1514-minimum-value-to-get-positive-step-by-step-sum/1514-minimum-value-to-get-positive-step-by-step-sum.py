class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sums = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sums.append(nums[i] + prefix_sums[i -1])
        
        min_value = min(prefix_sums)
        if min_value <= 0:
            return abs(min_value) + 1
        
        return 1
            
        