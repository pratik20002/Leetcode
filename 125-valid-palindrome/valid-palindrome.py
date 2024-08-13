class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanString = re.sub(r'[\W_]+', '', s)
        print(cleanString.lower())
        print( cleanString.lower()[::-1])
        if(cleanString.lower() == cleanString.lower()[::-1]):
            return True
        else:
            return False