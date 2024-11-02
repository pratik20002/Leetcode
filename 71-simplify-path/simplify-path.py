class Solution:
    def simplifyPath(self, path: str) -> str:
        elements = path.split("/")
        stack = []
        for element in elements:
            if element == "..":
                if stack:
                    stack.pop()
            elif element and element != ".":
                stack.append(element)
        
        return "/" + "/".join(stack)