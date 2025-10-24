class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        set_arr = set(arr)
        count = 0
        for element in arr:
            if element + 1 in set_arr:
                count += 1
        return count