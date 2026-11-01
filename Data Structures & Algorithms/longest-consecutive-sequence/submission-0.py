class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        long_seq = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                length = 1
                while num +1 in nums_set:
                    length += 1
                    num += 1
                long_seq = max(long_seq, length)
        return long_seq
