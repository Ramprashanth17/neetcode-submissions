from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""
        
        need = Counter(t)
        window = Counter()

        required_matching = len(need)
        current_matched = 0 

        best_len = float("inf")
        best_start = 0
        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] += 1
            
            if char in need and window[char] == need[char]:
                current_matched += 1
            
            while current_matched == required_matching:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left
                
                left_char = s[left]
                window[left_char] -= 1
                
                if left_char in need and window[left_char] < need[left_char]:
                    current_matched -= 1 
                left += 1
        
        if best_len == float("inf"):
            return ""
        
        return s[best_start:best_start + best_len]
        