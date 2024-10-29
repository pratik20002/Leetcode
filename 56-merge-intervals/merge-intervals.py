class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        out = [intervals[0]]

        for start2, end2 in intervals[1:]:
            end1 = out[-1][1]

            if end1 >= start2:
                out[-1][1] = max(end1, end2)
            
            else:
                out.append([start2, end2])
            
        return out
