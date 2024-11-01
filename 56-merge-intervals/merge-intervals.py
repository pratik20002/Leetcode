class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        res = [intervals[0]]

        for start2, end2 in intervals[1:]:
            end1 = res[-1][1]

            if end1 >= start2:
                res[-1][1] = max(end1, end2)
            
            else:
                res.append([start2, end2])
        
        return res
