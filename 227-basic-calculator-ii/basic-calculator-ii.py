class Solution:
    def calculate(self, s: str) -> int:
        result = 0  # Final result
        last_op_val = 0  # Last operation value for handling *, /
        current_number = 0  # Current number being built
        operator = '+'  # Start with '+' as the initial operator
        
        # Iterate through the string
        for i, char in enumerate(s):
            # Build the current number if it's a digit
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            
            # If char is an operator or the last character, process current number
            if char in "+-*/" or i == len(s) - 1:
                if operator == '+':
                    result += last_op_val  # Commit the last operation
                    last_op_val = current_number  # Set new last_op_val for +
                elif operator == '-':
                    result += last_op_val  # Commit the last operation
                    last_op_val = -current_number  # Set new last_op_val for -
                elif operator == '*':
                    last_op_val *= current_number  # Apply multiplication directly to last_op_val
                elif operator == '/':
                    # Apply integer division directly to last_op_val (truncate towards zero)
                    last_op_val = int(last_op_val / current_number)
                
                # Update the operator and reset current number
                operator = char
                current_number = 0
        
        # Add the last operation value to the result
        result += last_op_val
        return result