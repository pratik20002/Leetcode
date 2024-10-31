class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in index_dict:
                return [i, index_dict[diff]]
            
            index_dict[num] = i
        
