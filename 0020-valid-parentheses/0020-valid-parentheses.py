class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if (s.count("{") != s.count("}")) or (s.count("[") != s.count("]")) or (s.count("(") != s.count(")")):
            return False

        stack = []
        map_open = {"(": ")", "{": "}", "[": "]"}
        map_close = {")": "(", "}": "{", "]": "["}
        for i, c in enumerate(s):
            if map_open.get(c, False):
                # Open parentheses
                stack.insert(0, c)
                continue
            else:
                # Close parentheses
                if not stack:
                    return False
                if map_close.get(c, None) == stack[0]:
                    stack.remove(map_close[c])
                else:
                    return False

        return not bool(stack)