class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        for num in nums:
            seen.add(num)
        for num in range(len(nums) + 1):
            if num not in seen:
                return num
        