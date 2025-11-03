from collections import Counter


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        
        left = 0
        answer = 0
        for right in range(1, len(s) + 1):
            sub_array = s[left: right]
            window_counter = Counter(sub_array)
            condition = all([v == 1 for k,v in window_counter.items()])
            if not condition:
                left +=1
                continue
            answer = max(answer, len(sub_array))
        return answer