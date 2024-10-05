class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        cur = prev = res = 0

        cur_operation = '+'

        while i < len(s):
            curr_char = s[i]
            if curr_char.isdigit():
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1
                
                i -= 1
                
                if cur_operation == '+':
                    res += cur
                    prev = cur

                elif cur_operation == '-':
                    res -= cur
                    prev =-cur

                elif cur_operation == '*':
                    res -= prev
                    res += prev * cur
                    prev = cur * prev
                
                else:
                    res -= prev
                    res += int(prev/cur)

                    prev = int(prev/cur)

                cur = 0

            elif curr_char != " ":
                cur_operation = curr_char
        
            i += 1        
    
        return res