class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #O(N log n)
        # squared = [x ** 2 for x in nums]
        # squared.sort()
        # return squared
        

        # O(N)
        left, right = 0, len(nums) - 1
        result = [0] * len(nums)
        position = len(nums) - 1

        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            if left_square > right_square:
                result[position] = left_square
                left += 1
            
            else:
                result[position] = right_square
                right -= 1
            
            position -= 1

        return result
