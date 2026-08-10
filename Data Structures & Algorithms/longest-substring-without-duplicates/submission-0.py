class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        word_list = {} 
        max_len = 0
        for index, char in enumerate(s):
            if char in word_list and word_list[char] >= left:
                left = word_list[char] + 1
            
            word_list[char] = index
            max_len = max(max_len, index - left + 1)

        return max_len            