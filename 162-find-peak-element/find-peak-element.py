class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # left, right = 0, len(nums)

        # while left <= right:
        #     mid = (left + right) // 2
        #     mid_val = nums[mid]
        #     to_left = nums[mid - 1] if mid > 0 else float("-inf")
        #     to_right = nums[mid + 1] if mid < len(nums) - 1 else float("-inf")

        #     if to_left < mid_val > to_right:
        #         return mid
            
        #     elif to_left < mid_val < to_right:
        #         left = mid + 1
            
        #     else:
        #         right = mid - 1


        left, right = 0, len(nums)

        while left <= right:
            mid = (left + right) // 2
            
            mid_val = nums[mid]

            to_left = nums[mid - 1] if mid > 0 else float("-inf")
            to_right = nums[mid + 1] if mid < len(nums) - 1 else float("-inf")

            if to_left < mid_val > to_right:
                return mid
            
            elif to_left < mid_val < to_right:
                left = mid + 1
            
            else:
                right = mid - 1
