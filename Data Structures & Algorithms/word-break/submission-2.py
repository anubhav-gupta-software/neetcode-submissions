class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # for a particular j, canmake[j] = True if any i from 0 to j can be made and the other is valid. 

        n = len(s)
        words = set(wordDict)
        canMake = [False] * (n+1)
        canMake[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if canMake[j] and s[j:i] in words:
                    canMake[i] = True
                    break
        
        return canMake[n]