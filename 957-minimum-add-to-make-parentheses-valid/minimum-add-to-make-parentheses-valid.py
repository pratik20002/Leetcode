class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        unmatched_closing = 0

        for char in s:
            if char == "(":
                balance += 1
            
            elif char == ")":
                if balance > 0:
                    balance -= 1
                
                else:
                    unmatched_closing += 1
            
        return (balance + unmatched_closing)