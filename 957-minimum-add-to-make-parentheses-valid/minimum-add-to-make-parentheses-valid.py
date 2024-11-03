class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        unmatched_closing = 0

        for char in s:
            if char == "(":
                balance += 1 #balance = 3
            
            elif char == ")":
                if balance > 0:
                    balance -= 1 #balance = 0
                
                else:
                    unmatched_closing += 1 #unm = 1
            
        return (balance + unmatched_closing) 
