class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []

        # define backtrack function and parameters
        def backtrack(start:int, current:List[int]) -> None:
            """
            current: an list of current answer 
            remaining: an list of remaining numbers
            """
            
            ans.append(current.copy())
          


            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                current.append(nums[i])
                backtrack(i+1, current) 
                current.pop()
        
        nums.sort()
        backtrack(0, [])
        return ans