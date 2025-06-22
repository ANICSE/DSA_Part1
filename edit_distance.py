def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    #Crating a (m+1) x (nx1) DP table and initializing with zeros
    dp = [[0] * (n+1) for _ in range(m+1)]
    # for row in dp:
    #     print(row)
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    for row in dp:
        print(row) 

    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i -1] == word2[j -1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j], #Deletion
                    dp[i][j-1], #Insertion
                    dp[i-1][j-1] #Subsitution
                )  
    return dp[m][n]

def main():
    # m, n = 5,5
    # dp = [[0] * (n+1) for _ in range(m+1)]
    # for row in dp:
    #     print(row)
    s1 = "kitten"
    s2 = "sitting"
    print(f"Edit distance between '{s1}' and '{s2}': {edit_distance(s1, s2)}")

if __name__ == "__main__":
    main()

    