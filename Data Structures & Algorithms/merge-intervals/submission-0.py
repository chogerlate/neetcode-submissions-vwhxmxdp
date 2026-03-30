class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        merged_intervals = []
        
        for interval in sorted_intervals:
            start, end = interval[0], interval[1]
            match = False
            for existing_interval in merged_intervals:
                if existing_interval[0] <= start <= existing_interval[1] :
                    existing_interval[1] = end if existing_interval[1] < end else existing_interval[1]
                    match = True
                    break
            if not match :
                merged_intervals.append(interval)

        return merged_intervals