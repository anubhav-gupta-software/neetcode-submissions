class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #lcs[a][b] = lcs[a - 1][b - 1] + 1 if equal, lcs[a][b-1], lcs[a - 1][b]

        if len(text1) < len(text2):
            text1, text2 = text2, text1
        n1 = len(text1)
        n2 = len(text2)

        prev = [0] * (n2+1)

        for i in range(1, n1 + 1):
            curr = [0] * (n2 + 1)
            for j in range(1, n2 + 1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr
        
        return prev[n2]

