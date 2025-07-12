class Interval(object):
    def __init__(self, start, end):
        self.start= start
        self.end = end
        
class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key = lambda i: i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False
        return True
    
def main():
    # Example 1: Overlapping intervals
    meetings1 = [
        Interval(0, 30),
        Interval(5, 10),
        Interval(15, 20)
    ]
    
    # Example 2: Non-overlapping intervals
    meetings2 = [
        Interval(0, 5),
        Interval(5, 10),
        Interval(10, 15)
    ]

    sol = Solution()
    
    print("Can attend all meetings in meetings1:", sol.canAttendMeetings(meetings1))  # Expected: False
    print("Can attend all meetings in meetings2:", sol.canAttendMeetings(meetings2))  # Expected: True

if __name__ == "__main__":
    main()