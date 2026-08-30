class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_d = Counter(s1)
        n = len(s1)
        s2_d = {}
        l = 0
        
        for r in range(len(s2)):
            s2_d[s2[r]] = s2_d.get(s2[r], 0) + 1
            if r - l + 1 > n:
                s2_d[s2[l]] -= 1
                if s2_d[s2[l]] == 0:
                    del s2_d[s2[l]]
                l += 1
            if r - l + 1 == n and s2_d == s1_d:
                return True
        
        return False