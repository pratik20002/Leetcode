class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #O(N log n)
        squared = [x ** 2 for x in nums]
        squared.sort()
        return squared
        

