class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        equal_chars = []
        lower_lenght = min([len(item) for item in strs])
        for i in range(lower_lenght):
            i_chars = [item[i] for item in strs]
            ok = all(i_char == i_chars[0] for i_char in i_chars)
            if not ok:
                break
            if ok:
                equal_chars.append(i)

        if equal_chars:
            same_prefix_size = max(equal_chars)
            return strs[0][:same_prefix_size + 1]
        else:
            return ""