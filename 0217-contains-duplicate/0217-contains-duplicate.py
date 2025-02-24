class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mapping = {}
        for num in nums:
            if mapping.get(num):
                mapping[num] += 1
            else:
                mapping[num] = 1
            if mapping.get(num, 0) > 1:
                return True
        return False