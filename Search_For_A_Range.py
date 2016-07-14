class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if nums is None:
            return [-1, -1]
            
        start, end = 0, len(nums)-1
        left, right = -1, -1
        # Find left bound
        while start+1<end:
            mid = start + (end-start)/2
            if nums[mid]==target:
                end = mid
            elif nums[mid]<target:
                start = mid
            else:
                end = mid
        
        if nums[start]==target:
            left = start
        elif nums[end]==target:
            left = end
        else:
            left, right = -1, -1
            return [left, right]
        
        start, end = 0, len(nums)-1
        # Find right bound
        while start+1<end:
            mid = start + (end-start)/2
            if nums[mid]==target:
                start = mid
            elif nums[mid]<target:
                start = mid
            else:
                end = mid
        
        if nums[end]==target:
            right = end
        elif nums[start]==target:
            right = start
        else:
            left, right = -1, -1
        
        return [left, right]

A = [1,2,3,4,5,5,5,5,5,5,6,8]
sol = Solution()
print sol.searchRange(A, 5)