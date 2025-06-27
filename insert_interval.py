from typing import List
class solution:
    def inert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i, n = 0, len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i+= 1
        mI = newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            mI[0] = min(mI[0], intervals[i][0])
            mI[1] = max(mI[1], intervals[i][1])
            
            i+=1
        result.append(mI)

        while i < n:
            result.append(intervals[i])
            i+= 1

        return result

def main():
    sol = solution()
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print(f"After insertion: {sol.inert(intervals, newInterval)}")  # Expected: [[1,5],[6,9]]

    intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval2 = [4,8]
    print(f"After insertion: {sol.inert(intervals2, newInterval2)}")  # Expected: [[1,2],[3,10],[12,16]]

if __name__ == "__main__":
    main()    