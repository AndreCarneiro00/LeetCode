class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match = {"(": ")", "{": "}", "[": "]"}
        for char in s:
            if not stack:
                stack.append(char)
                continue

            top = stack[-1]
            print(top, char)
            if match.get(top) == char:
                stack.pop()
            else:
                stack.append(char)
        print(stack)
        return len(stack) == 0