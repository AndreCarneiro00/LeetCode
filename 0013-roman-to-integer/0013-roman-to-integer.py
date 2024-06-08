class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_values = {"I": 1,
                         "V": 5,
                         "X": 10,
                         "L": 50,
                         "C": 100,
                         "D": 500,
                         "M": 1000}
        len_s = len(s)
        result = 0
        for i in range(len_s):
            symbol_value_0 = symbol_values.get(s[len_s - i - 1])
            symbol_value_1 = 0
            symbol_value_2 = 0
            symbol_value_3 = 0
            if len_s - i - 1 >= 0 and symbol_value_0 > symbol_values.get(s[len_s - i - 1]):
                symbol_value_1 = symbol_values.get(s[len_s - i - 1]) * 2
            if len_s - i  -2 >= 0 and symbol_value_0 > symbol_values.get(s[len_s - i  -2]):
                symbol_value_2 = symbol_values.get(s[len_s - i  -2]) * 2
            if len_s - i - 3 >= 0 and symbol_value_0 > symbol_values.get(s[len_s - i - 3]):
                symbol_value_3 = symbol_values.get(s[len_s - i - 3]) * 2
            value = symbol_value_0 - symbol_value_2 - symbol_value_1 - symbol_value_3
            result += value

        return result