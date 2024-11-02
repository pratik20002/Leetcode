class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        cnt = 0
        for char in s:
            if char == "(":
                res.append(char)
                cnt += 1
            elif char == ")" and cnt > 0:
                res.append(char)
                cnt -= 1
            elif char != ")":
                res.append(char)
            
        filtered_str = []
        for char in res[::-1]:
            if char == "(" and cnt > 0:
                cnt -= 1
            else:
                filtered_str.append(char)
        
        return "".join(filtered_str[::-1])