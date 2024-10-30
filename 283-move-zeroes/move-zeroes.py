class Solution:
    def moveZeroes(self, nums: List[int]) -> List:
        insert_pos = 0

        for num in nums:
            if num:
                nums[insert_pos] = num
                insert_pos += 1
            
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1
        
        return nums