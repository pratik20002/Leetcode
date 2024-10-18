class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        rows = len(nums)

        v = []
        for x in range(rows):
            for y in range(len(nums[x])):
                v.append((x + y, y, nums[x][y]))
        
        res = list(x[2] for x in sorted(v))
        return res