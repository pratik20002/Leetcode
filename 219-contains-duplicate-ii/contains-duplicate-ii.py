class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numDict = {}
        for idx in range(len(nums)):
            if nums[idx] in numDict:
                if abs(idx - numDict[nums[idx]]) <= k:
                    return True
            numDict[nums[idx]] = idx
        return False

