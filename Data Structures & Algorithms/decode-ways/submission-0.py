class Solution:
    def numDecodings(self, s: str) -> int:
        #no of ways = no of ways - 1
        #if s[curr - 1] == 1 or 2: then no of ways = (no of ways - 1) + (no of ways - 2)
        #"0"  together then not "00"
        
        n = len(s)
        if s[0] == "0":
            return 0

        if n == 1:
            return 1
        ways = [1] * n
        for i in range(1, n):
                
            if s[i] == "0" and s[i - 1] == "0":
                return 0
            if s[i] == "0" and s[i-1] in "12":
                ways[i] = ways[i - 2]
                continue
            if s[i] == "0" and s[i-1] not in "12":
                return 0
            ways[i] = ways[i - 1]
            if s[i - 1] == "1" or (s[i - 1] == "2" and s[i] in "123456"):
                if i == 1:
                    ways[i] += 1
                else:
                    ways[i] += ways[i - 2]
        return ways[n - 1]