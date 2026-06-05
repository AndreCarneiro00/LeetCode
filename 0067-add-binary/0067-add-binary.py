from collections import deque

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = int(max(len(a), len(b)))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        result = deque()
        add_one = False
        for i in range(len(a) -1, -1, -1):
            summed = int(a[i]) + int(b[i]) + add_one
            if summed == 2:
                summed = 0
                add_one = True
            elif summed == 3:
                summed = 1
                add_one = True
            else:
                add_one = False
            
            result.appendleft(str(summed))
        
        if add_one:
            result.appendleft("1")

        return "".join(result)
            