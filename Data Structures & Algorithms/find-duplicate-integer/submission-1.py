class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq_map = {}
        for index, num in enumerate(nums):
            freq_map[num] = freq_map.get(num, 0) + 1
            if freq_map[num] > 1:
                return num