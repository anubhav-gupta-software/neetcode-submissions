class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_l, best_r = 0,0
        
        #odd
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if best_r - best_l < r - l:
                    best_l, best_r = l, r
                l -= 1
                r += 1

        #even
        for i in range(len(s)):
                l, r = i - 1, i
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if best_r - best_l < r - l:
                        best_l, best_r = l, r
                    l -= 1
                    r += 1
        return s[best_l: best_r + 1]