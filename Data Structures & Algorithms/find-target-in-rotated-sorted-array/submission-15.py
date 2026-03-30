class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Simulation: 
            [3,4,5,6,1,2]
                 ^
            just like the previous question but instead of saving the value save the position instead
        """
        left, right = 0, len(nums)-1
        pivot = 0
        # get the amount of time rotation applied
        while left <= right :
            mid = (left + right) // 2
            pivot = mid if nums[mid] < nums[pivot] else pivot
            if nums[mid] < nums[right]:
                right = mid - 1
            else :
                left = mid + 1
        print(pivot)
        # search left and right 
        def bfs(arr: list[int], target):
            left, right = 0, len(arr)-1
            print(arr)
            while left <= right :
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else :
                    right = mid -1
            return -1 
        
        left, right = 0, len(nums)-1
        left_idx = bfs(nums[:pivot], target)
        print("left idx: ", left_idx)
        right_idx = bfs(nums[pivot:], target)
        print("right idx: ", right_idx)
        if left_idx != -1 :
            return left_idx
        elif right_idx != -1 :
            return pivot + right_idx 
        else :
            return -1