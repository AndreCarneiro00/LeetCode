class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst_len = len(nums)
        for i in range(lst_len):
            for j in range(lst_len):
                if (nums[i] + nums[j] == target) and (i != j):
                    return [i, j]