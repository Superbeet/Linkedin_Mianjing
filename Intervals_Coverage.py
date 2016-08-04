
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# O(n)
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
            
        intervals.append(newInterval)
        # intervals = sorted(intervals, key=lambda obj:[obj.start, obj.end], reverse=False)
        
        before = []
        after = []
        
        for i in xrange(0, len(intervals)):
            
            if newInterval.start > intervals[i].end:
                before.append(intervals[i])
            
            if newInterval.start >= intervals[i].start and newInterval.start <= intervals[i].end:
                newInterval.start = min(intervals[i].start, newInterval.start)
            
            if newInterval.end <= intervals[i].end and newInterval.end >= intervals[i].start:
                newInterval.end = max(intervals[i].end, newInterval.end)
            
            if newInterval.end < intervals[i].start:
                after.append(intervals[i])
        
        res = before
        res.append(newInterval)
        res.extend(after)
        
        return res

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# O(nlogn) better than O(n*n) repeatly run above method
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
         
        res = []
        
        intervals = sorted(intervals, key=lambda obj:[obj.start,obj.end], reverse= False)
        
        prev = intervals[0]
        
        for i in xrange(1, len(intervals)):
            cur = intervals[i]
            if prev.end >= cur.start:
                prev.end = max(prev.end, cur.end)
            else:
                res.append(prev)
                prev = cur
                
        res.append(prev)
        return res
                
        