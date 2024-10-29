class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        
        p1 = p2 = 0
        res = []

        while p1 < len(firstList) and p2 < len(secondList):
            start1, end1 = firstList[p1]
            start2, end2 = secondList[p2]

            start = max(start1, start2)
            end = min(end1, end2)

            if start <= end:
                res.append([start, end])
            if end1 < end2:
                p1 += 1
            else:
                p2 += 1
            
        return res