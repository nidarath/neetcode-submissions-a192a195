"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #sort by beginning values in-place
        intervals.sort(key = lambda x: x.start) #sort by the start of each interval
        for i in range(1, len(intervals)): #from 1 to end
            # if they overlap return false
            i1 = intervals[i - 1]#first ending
            i2 = intervals [i] #second beginning
            if i1.end > i2.start:
                return False
        return True
        #error i ran into was using x[0], but we are using interval class at the top not a list 

        #Time complexity is (nlogn) bc for n items, we sort
        #space O(1) because we sort in place but O(n) due to our sorting method 
        