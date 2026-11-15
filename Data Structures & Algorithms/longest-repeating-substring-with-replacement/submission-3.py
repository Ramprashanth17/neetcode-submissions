class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        left = 0
        max_freq = 0
        max_window = 0

        for right in range(0, len(s)):
            freq[ord(s[right]) - 65] += 1
            max_freq = max(max_freq, freq[ord(s[right]) - 65])
            window_length = right - left + 1
            while window_length - max_freq > k:
                freq[ord(s[left]) - 65] -= 1
                left += 1
                window_length = right - left + 1
            
            max_window = max(max_window, window_length)
        return max_window
            