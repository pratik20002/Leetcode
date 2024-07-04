class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if max(Counter(nums).values()) > 1:
            return True
        else:
            return False