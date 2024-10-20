class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        # picked_index = 0
        # count = 0

        # for i, num in enumerate(self.nums):
        #     if num == target:
        #         count += 1

        #         if random.randint(1, count) == count:
        #             picked_index = i
            
        # return picked_index
        while True:
            index = randint(0, len(self.nums) - 1)
            if target == self.nums[index]:
                return index
        





# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)