class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ''.join(char.lower() for char in s if char.isalnum() )
        reversed_s = ''.join(cleaned_s[::-1])
        return cleaned_s == reversed_s