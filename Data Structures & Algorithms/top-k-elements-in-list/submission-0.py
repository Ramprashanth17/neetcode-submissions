class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1 ## {1:1, 2:2, 3:3}
        sorted_nums = sorted(hashmap.items(), key= lambda x: x[1], reverse = True)
        return [item[0] for item in sorted_nums[:k]]


