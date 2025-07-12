class Interval(object):
    def __init__(self, start, end):
        self.start= start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals):
        start = sorted([i.start for i in intervals ])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count +=1
            else:
                e +=1
                count -= 1

            res = max(res, count)
        return res

def main():
    meetings1 = [
        Interval(0, 30),
        Interval(5, 10),
        Interval(15, 20)
    ]  # Overlaps — needs 2 rooms

    meetings2 = [
        Interval(0, 5),
        Interval(5, 10),
        Interval(10, 15)
    ]  # No overlap — only 1 room needed

    sol = Solution()
    print("Minimum meeting rooms for meetings1:", sol.minMeetingRooms(meetings1))  # Expected: 2
    print("Minimum meeting rooms for meetings2:", sol.minMeetingRooms(meetings2))  # Expected: 1

if __name__ == "__main__":
    main()
