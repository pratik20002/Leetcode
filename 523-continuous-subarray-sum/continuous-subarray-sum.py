class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0 : -1}
        total = 0

        for i, num in enumerate(nums):
            total += num
            r = total % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True
        
        return False

        #23,2,4,6,7
        
        #23,2,6,4,7