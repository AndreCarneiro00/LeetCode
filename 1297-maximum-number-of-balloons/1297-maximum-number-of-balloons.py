from collections import Counter


class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        balloon
        """
        char_counter = Counter(text)
        return min((char_counter.get("b", 0), char_counter.get("a", 0), char_counter.get("l", 0)//2, char_counter.get("o", 0)//2, char_counter.get("n", 0)))