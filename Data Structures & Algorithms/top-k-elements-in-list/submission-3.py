class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can simply use counter dict 
        nums_counter = Counter(nums)
        # we then sort the res by counter values we problably use heap to help build query tree with O(log n) serach time
        from heapq import heappop, heappush
        heap = [] 

        for val,freq in nums_counter.items():
            item = (freq, val)
            heappush(heap, item)

            if len(heap) > k :
                heappop(heap) 
        
        return [ h[1] for h in heap ]

        