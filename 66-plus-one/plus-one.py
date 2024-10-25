class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = ""
        for num in digits:
            total += str(num)
        total = int(total) + 1
        return [int(digit) for digit in str(total)]
