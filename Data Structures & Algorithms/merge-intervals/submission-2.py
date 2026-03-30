class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        merged_intervals = []
        
        for interval in sorted_intervals:
            start, end = interval[0], interval[1]
            match = False
            if merged_intervals and merged_intervals[-1][0] <= start <= merged_intervals[-1][1] :
                merged_intervals[-1][1] = end if merged_intervals[-1][1] < end else merged_intervals[-1][1]
                match = True
            if not match :
                merged_intervals.append(interval)

        return merged_intervals