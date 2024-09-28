class Solution:
    def isPalindrome(self, s: str) -> bool:
        #cleanString = re.sub(r'[\W_]+', '', s)

        # if(cleanString.lower() == cleanString.lower()[::-1]):
        #     return True
        # else:
        #     return False

        # cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
        # left, right = 0, len(cleaned_string) - 1

        # while left < right:
        #     if cleaned_string[left] != cleaned_string[right]:
        #         return False
        #     left += 1
        #     right -= 1

        # return True

        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not self.isalphaNum(s[left]):
                left += 1
            while right > left and not self.isalphaNum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        
        return True

    
    def isalphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

            