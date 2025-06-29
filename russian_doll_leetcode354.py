import bisect
from typing import List

class Solution:
    def russian_doll(self, envelopes: List[List[int]])-> int:
        #sort based on width
        envelopes.sort(key=lambda x : (x[0], -x[1]))

        #extract heights
        heights = [h for w, h in envelopes]

        dp = []
        for h in heights:
            idx = bisect.bisect_left(dp, h)
            if idx == len(dp):
                dp.append(h)
            else:
                dp[idx] = h
        return len(dp)
    
def main():
    sol = Solution()
    envelopes = [[5,4], [6,4], [6,7], [2,3]]
    print(f"the LIS in envelopes {envelopes} is : {sol.russian_doll(envelopes)}")

if __name__ == "__main__":
    main()