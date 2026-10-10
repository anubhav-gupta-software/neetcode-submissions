class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pal = s[0]
        
        #odd
        for i in range(1, len(s)):
            x, y = i, i
            while s[x] == s[y]:
                new_pal = s[x:y + 1]
                if len(max_pal) < len(new_pal):
                    max_pal = new_pal
                x, y = x - 1, y + 1
                if x < 0 or y >= len(s):
                    break

        #even
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                x = i - 1
                y = i
                while s[x] == s[y]:
                    new_pal = s[x:y + 1]
                    if len(max_pal) < len(new_pal):
                        max_pal = new_pal
                    x, y = x - 1, y + 1
                    if x < 0 or y >= len(s):
                        break
        return max_pal