class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #lcs[a][b] = lcs[a - 1][b - 1] + 1 if equal, lcs[a][b-1], lcs[a - 1][b]

        n1 = len(text1)
        n2 = len(text2)
        lcs = [[0] * (n2+1) for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
                if text1[i-1] == text2[j-1]:
                    lcs[i][j] = max(lcs[i][j], lcs[i-1][j-1] + 1)
        
        return lcs[n1][n2]

