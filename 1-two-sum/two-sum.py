class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap ={}

        #1st Pass
        for i, num in enumerate(nums):
            numMap[num] = i

        #2nd Pass
        for i, num in enumerate(nums):
            diff = target - num
            if diff in numMap and numMap[diff] != i:
                return [i, numMap[diff]]
        
        return []