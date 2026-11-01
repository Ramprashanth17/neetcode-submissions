class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        # if len(s) != len(t):
        #     return False
        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1
        for char in t:
            if char not in hash_map:
                return False
            else:
                hash_map[char] -= 1
        return all(count == 0 for count in hash_map.values())