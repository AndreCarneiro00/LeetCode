class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        if nums_len == 1 and k > 0:
            return [-1]
        if nums_len == 1 and k == 0:
            return [nums[0]]
        
        prefix_sum = [nums[0]]
        for i in range(1, nums_len):
            prefix_sum.append(nums[i] + prefix_sum[i - 1])
        print(prefix_sum)
        k_avg_array = []
        for i, num in enumerate(nums):
            if i - k < 0 or i + k + 1 > nums_len:
                k_avg_array.append(-1)
                continue
                
            limit_i = i - k
            limit_j = i + k
            print(limit_i)
            print(limit_j)

            avg = (prefix_sum[limit_j] - prefix_sum[limit_i] + nums[limit_i]) // (limit_j - limit_i + 1)
            k_avg_array.append(avg)
            
        return k_avg_array