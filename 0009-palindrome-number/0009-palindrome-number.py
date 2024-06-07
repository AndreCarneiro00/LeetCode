class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        len_s = len(s)
        lst_bool = []
        for i in range(len_s):
            if s[i] == s[len_s - i - 1]:
                lst_bool.append(True)
            else:
                lst_bool.append(False)
        return all(lst_bool)
