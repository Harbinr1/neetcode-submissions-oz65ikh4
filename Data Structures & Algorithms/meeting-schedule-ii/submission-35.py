"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        import heapq
        intervals.sort(key = lambda x:x.start)
        heap = []
        rooms = 0

        for meet in intervals:
            if heap and heap[0] <= meet.start:
                heapq.heappop(heap)
            heapq.heappush(heap,meet.end)
            rooms = max(rooms,len(heap))
        return rooms

        