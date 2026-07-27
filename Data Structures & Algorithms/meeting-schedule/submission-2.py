"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# when meetings ends at the same time one starts they don't overlap.
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort through meetings by the starting time
        # what this function does is take a key to sort by where 
        # i is a placeholder that takes the start value.
        intervals.sort(key=lambda i:i.start)
        
        #from the second meeting to the end
        #compare the meetings
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            #if any overlap return false
            if i1.end > i2.start:
                return False
        return True   

    # this is O(nlogn) because the algorithm divides the list in half
    # repeatedly to sort the list and the for loop is linear with
    # n items, so n times logn
    
