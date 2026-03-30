class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        res = r
        
        def totalhr(k, piles):
            return sum([ -(-x//k) for x in piles])
        
        while r >= l :
            k = l + (r-l)//2
            if totalhr(k, piles) <= h :
                res = k
                r = k-1
            else :
                l = k+1

        return res
                    