class Solution:
    def numDecodings(self, s: str) -> int:
        #1-9, no of ways = no of ways - 1
        #0, no of ways = no of ways - 2 if and only if s[i-1] == 1 or 2 else return 0
        #1-9, and s[i-1] = 1 or s[i-1] = 2 and 1-6 then += no of ways - 2
        n = len(s)
        if s[0] == "0":
            return 0
        prev, curr = 1, 1
        for i in range(1, n):
            new = 0
            if s[i] != "0":
                new = curr
            if s[i - 1] == "1" or (s[i-1] == "2" and s[i] in "0123456"):
                new += prev
            
            prev, curr = curr, new
        
        return curr
