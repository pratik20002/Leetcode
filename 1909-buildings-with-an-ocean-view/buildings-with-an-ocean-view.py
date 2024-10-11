class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        out = []
        maxHeight = 0
        for i in range((len(heights) - 1), -1, -1):
            if heights[i] > maxHeight:
                out.append(i)
                maxHeight = heights[i]

        return out[::-1]