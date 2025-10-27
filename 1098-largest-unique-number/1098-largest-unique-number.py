from collections import defaultdict

class Solution(object):
    def largestUniqueNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
        
        result = -1
        for num, count in count_map.items():
            if count == 1:
                result = max(result, num)
                
        return result
        