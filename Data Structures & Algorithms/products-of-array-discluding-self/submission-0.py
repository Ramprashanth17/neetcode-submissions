class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(0, len(nums)):
            product = 1
            for j in range(0, len(nums)):
                if j != i:
                    product *= nums[j]
            answer.append(product)
        return answer

