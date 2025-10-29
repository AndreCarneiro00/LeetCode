from collections import Counter

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        stones_counter = Counter(stones)
        count = 0
        for k, v in stones_counter.items():
            if k in jewels:
                count += v
                
        return count