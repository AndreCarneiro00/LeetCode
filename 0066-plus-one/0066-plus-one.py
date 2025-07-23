class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [str(digit) for digit in digits]
        number = str(int("".join(digits)) + 1)
        new_array = [int(char) for char in number]
        return new_array