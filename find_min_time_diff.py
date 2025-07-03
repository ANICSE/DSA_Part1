from typing import List
class Solution:
    def min_time_diff(self, time: List[str]) -> int:
        minutes = []
        for t in time:
            h, m = map(int, t.split(":"))
            minutes.append(h * 60 + m)

        if len(minutes) > 1440:
            return 0
        minutes.sort() 
        min_diff = 1440

        #Check the adjacent_diff
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i-1])

        min_diff = min(min_diff, 1440 + minutes[0] - minutes[-1])
    
        return min_diff
    
def main():
    sol = Solution()
    time = ["01:10", "03:00", "22:30"]
    print(f"The min time difference between {time} is: {sol.min_time_diff(time)}")

if __name__ == "__main__":
    main()
        
