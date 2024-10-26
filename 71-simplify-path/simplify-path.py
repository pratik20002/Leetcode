class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        elements = path.split("/")

        for element in elements:
            if element == "" or element == ".":
                continue
            
            if element == "..":
                if stack:
                    stack.pop()
            
            else:
                stack.append(element)
            
        return "/" + "/".join(stack)
