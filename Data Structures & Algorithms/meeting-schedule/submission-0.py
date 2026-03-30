"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        interval_checker = []
        for interval in sorted_intervals:
            match_flag = False
            if interval_checker and interval_checker.start <= interval.start < interval_checker.end:
                return False
            
            if not match_flag:
                interval_checker = interval 


        return True