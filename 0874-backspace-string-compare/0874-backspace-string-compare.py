class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def build_stack(s):
            stack = []
            for c in s:
                if stack and c == "#":
                    stack.pop()
                elif c == "#":
                    continue
                else:
                    stack.append(c)
            
            return stack

        return build_stack(s) == build_stack(t)