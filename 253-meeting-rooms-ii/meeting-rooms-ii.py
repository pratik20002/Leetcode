class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # intervals = sorted(intervals)
        # print(intervals)
        # conCount = 1

        # for i in range(1, len(intervals)):
        #     m1 = intervals[i-1][1]
        #     m2 = intervals[i][0]

        #     if m1 > m2:
        #         conCount += 1

        # return conCount

        start = sorted([interval[0] for interval in intervals])
        end = sorted([interval[1] for interval in intervals])

        res, count = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if(start[s] < end[e]):
                s += 1
                count += 1       
            else:
                e += 1
                count -= 1
            res = max(res, count)
    
        return res