class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_Counter = 0
        res = 0
        for c in s:
            if c == "(":
                open_Counter += 1
            else:
                if open_Counter == 0:
                    res += 1
                open_Counter = max(open_Counter - 1, 0)
            
        return res + open_Counter
