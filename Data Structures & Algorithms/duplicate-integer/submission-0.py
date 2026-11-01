class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for n in nums:
            hash_map[n] = hash_map.get(n, 0) + 1
            if hash_map[n] > 1:
                return True
        return False