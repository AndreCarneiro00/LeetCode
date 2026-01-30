class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            left_char = s[left]
            s[left] = s[right]
            s[right] = left_char
            left += 1
            right -= 1
        
        return "".join(s)

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        return " ".join(list(map(self.reverseString, words)))
        

