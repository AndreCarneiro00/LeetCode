class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        result = -1
        i = j = 0
        while i < len(nums1) and j < len(nums2) :
            if nums1[i] == nums2[j] and result == -1:
                result = nums1[i]
            elif nums1[i] == nums2[j]:
                result = min(nums1[i], result)

            if nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        
        return result