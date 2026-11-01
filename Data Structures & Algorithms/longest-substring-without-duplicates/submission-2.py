class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result, left, right = 0,0,0
        my_dict = {}
        while right < len(s):
            if s[right] in my_dict:
                left = max(left, my_dict[s[right]] + 1) 
            result = max(result, right - left + 1)
            my_dict[s[right]] = right
            right += 1
        return result