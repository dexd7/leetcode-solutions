class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Clarify:
        # - Intervals not sorted based on start time, I will have to do that.
        # - will be 2d List where each item List will contain only two numbers where start<=end
        # - intervals cannot be empty
        # I am thinking about maintaining a stack to keep track of all valid fully segregated intervals.
        # For each valid fully segregated interval, we need to maintain a starting point, which we can set as the start of the first interval
        # We will also maintain a current_end going through each iteration and every time we encounter a number greater than it we sent our current_start_flag to False to change it.
        #Going through each iteration we only change our start if we added a new interval.
        #
        intervals.sort(key=lambda x: x[0])
        merged = []
        curr_start, curr_end = intervals[0][0], intervals[0][1]
        start_change = False
        for i in range(1, len(intervals)):
            if curr_end<intervals[i][0]:
                merged.append([curr_start, curr_end])
                start_change = True
            curr_end = max(curr_end, intervals[i][1])
            if start_change:
                curr_start = intervals[i][0]
                start_change = False
        merged.append([curr_start,curr_end])
        return merged
