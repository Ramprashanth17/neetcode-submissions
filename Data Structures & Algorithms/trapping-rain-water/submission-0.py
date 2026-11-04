class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        total = 0
        lmax, rmax = 0,0
        while left < right:
            lmax = max(lmax, height[left])
            rmax = max(rmax, height[right])
            if lmax <= rmax:
                amount = min(lmax, rmax) - height[left]
                total += amount
                left += 1
            if lmax > rmax:
                amount = min(lmax, rmax) - height[right]
                total += amount
                right -= 1
    
        return total
        