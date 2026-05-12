class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for i in s:
            dict_s[i] = dict_s.get(i, 0) + 1
        
        for i in t:
            dict_t[i] = dict_t.get(i, 0) + 1

        return dict_t == dict_s
        #Counter is O(n)
        # if Counter(s) == Counter(t):
        #     return True
        # return False