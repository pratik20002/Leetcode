class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        cnt = 0

        for c in s:
            if c == "(":
                res.append(c)
                cnt += 1
            
            elif c == ")" and cnt > 0:
                res.append(c)
                cnt -= 1
            
            elif c != ")":
                res.append(c)

            
        filtered_str = []

        for element in res[::-1]:
            if element == "(" and cnt > 0:
                cnt -= 1
            else:
                filtered_str.append(element)

        return "".join(filtered_str[::-1])
            
