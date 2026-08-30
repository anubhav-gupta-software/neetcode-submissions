class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False
        
        need = Counter(s1)
        window = Counter(s2[:n])

        if need == window:
            return True

        for r in range(n, len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1
            left = r - n
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                del window[s2[left]]
            
            if window == need:
                return True
        
        return False
        
        return False
