class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}

        for i, num in enumerate(nums):
            to_search = target - num
            if to_search in index_dict:
                return [i, index_dict[to_search]]
            
            index_dict[num] = i
