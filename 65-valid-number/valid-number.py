class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()  
        if not s:
            return False  

        num_seen = False
        dot_seen = False
        exp_seen = False
        num_after_exp = True

        for i, char in enumerate(s):
            if char.isdigit():
                num_seen = True
                num_after_exp = True  
            elif char == '.':
                if dot_seen or exp_seen:
                    return False
                dot_seen = True
            elif char in 'eE':
                if exp_seen or not num_seen:
                    return False
                exp_seen = True
                num_after_exp = False  
            elif char in '+-':
                if i > 0 and s[i - 1] not in 'eE':
                    return False
            else:
                return False

        return num_seen and num_after_exp