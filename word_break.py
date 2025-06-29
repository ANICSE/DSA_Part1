from typing import List

class Solution:
    def wordbreak(self, s: str, worddict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in worddict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]

def main():
    sol = Solution()
    s = "leetcode"
    worddict = ["leet", "code"]
    print(f'Can "{s}" be segmented? {sol.wordbreak(s, worddict)}')  # Output: True

    s2 = "applepenapple"
    worddict2 = ["apple", "pen"]
    print(f'Can "{s2}" be segmented? {sol.wordbreak(s2, worddict2)}')  # Output: True

    s3 = "catsandog"
    worddict3 = ["cats", "dog", "sand", "and", "cat"]
    print(f'Can "{s3}" be segmented? {sol.wordbreak(s3, worddict3)}')  # Output: False

if __name__ == "__main__":
    main()

    

    