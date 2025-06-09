class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        should_pop = []
        seen_nums = []
        for i, num in enumerate(nums):
            if num in seen_nums:
                should_pop.append(i)
            seen_nums.append(num)

        for index in sorted(should_pop, reverse=True):
            del nums[index]

        return len(nums)