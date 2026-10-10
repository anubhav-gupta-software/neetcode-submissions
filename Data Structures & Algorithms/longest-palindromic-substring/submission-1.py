class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pal = s[0]
        
        #odd
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                new_pal = s[l:r + 1]
                if len(max_pal) < len(new_pal):
                    max_pal = new_pal
                l -= 1
                r += 1

        #even
        for i in range(len(s)):
                l, r = i - 1, i
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    new_pal = s[l:r + 1]
                    if len(max_pal) < len(new_pal):
                        max_pal = new_pal
                    l -= 1
                    r += 1
        return max_pal