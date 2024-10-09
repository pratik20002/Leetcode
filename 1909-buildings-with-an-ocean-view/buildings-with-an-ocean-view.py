class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        out = []
        maxheight = 0
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > maxheight:
                out.append(i)
                maxheight = heights[i]
        return out[::-1]
        