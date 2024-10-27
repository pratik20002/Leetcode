class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        for ch in s:
            if res and ch == res[-1]:
                res.pop()
            else:
                res.append(ch)

        return "".join(res)