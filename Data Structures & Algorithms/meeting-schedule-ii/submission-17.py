"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)
        total = 1
        if len(intervals) ==1:
            return total



        tmp_inter = []

        while intervals != []:
            start_tmp = intervals[0].start
            end_tmp = intervals[0].end
            for i in range(1, len(intervals)):
                # No conflict move next
                if end_tmp <= intervals[i].start:
                    # start_tmp = intervals[i].start
                    end_tmp = intervals[i].end
                # conflict, save and move
                else:
                    tmp_inter.append(intervals[i])
            if tmp_inter != []:
                total += 1
            tmp_inter, intervals = [], tmp_inter 

        return total