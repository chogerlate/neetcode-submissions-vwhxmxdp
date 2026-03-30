class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAll(k):
            # Helper function to check if Koko can eat all bananas at speed k within h hours
            totalTime = sum(math.ceil(float(p) / k) for p in piles)
            return totalTime <= h

        def binarySearch(l, r):
            if l > r:
                return l  # Base case: return the left boundary when it surpasses right
            
            k = (l + r) // 2
            
            if canEatAll(k):
                return binarySearch(l, k - 1)  # Try a smaller speed
            else:
                return binarySearch(k + 1, r)  # Try a larger speed
        
        return binarySearch(1, max(piles))