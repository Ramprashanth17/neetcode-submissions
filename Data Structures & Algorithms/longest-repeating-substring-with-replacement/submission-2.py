class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        alphabet_counts = [0] * 26

        for r in range(0, len(s)):
            alphabet_counts[ord(s[r]) - 65] += 1
            while (r-l + 1) - max(alphabet_counts) > k:
                alphabet_counts[ord(s[l]) - 65] -= 1
                l += 1
            
            longest = max(longest, (r-l+1))
        
        return longest