class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need = [0] * 26
        window = [0] * 26

        for i in range(len(s1)):
            need[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if need[i] == window[i]:
                matches += 1
        
        if matches == 26:
            return True
        
        for i in range(len(s1), len(s2)):
            idx = ord(s2[i]) - ord('a')
            if window[idx] == need[idx]:
                matches -= 1
            
            window[idx] += 1

            if window[idx] == need[idx]:
                matches += 1
            
            l = i - len(s1)
            idx = ord(s2[l]) - ord('a')
            
            if window[idx] == need[idx]:
                matches -= 1
            
            window[idx] -= 1

            if window[idx] == need[idx]:
                matches += 1
            
            if matches == 26:
                return True
        
        return False
