class Solution:
    def calculate(self, s: str) -> int:
         i = 0
         res = cur = prev = 0
         curr_operation = "+"

         while i < len(s):
            cur_char = s[i]
            if cur_char.isdigit():
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1
                i -= 1
                if curr_operation == "+":
                    res += cur
                    prev = cur
                
                elif curr_operation == "-":
                    res -= cur
                    prev = -cur

                elif curr_operation == "*":
                    res -= prev
                    res += prev * cur
                    prev = prev * cur

                else:
                    res -= prev
                    res += int(prev / cur)
                    prev = int(prev / cur)
                
                cur = 0
            
            elif cur_char != " ":
                curr_operation = cur_char
            
            i += 1
        
         return res
