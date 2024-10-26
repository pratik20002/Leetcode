class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append([char, 1])
            else:
                if char != stack[-1][0]:
                    stack.append([char, 1])
                else:
                    if stack[-1][1] + 1 == k:
                        stack.pop()
                    else:
                        stack[-1][1] += 1
        
        stack = [char * count for char, count in stack]
        return "".join(stack)