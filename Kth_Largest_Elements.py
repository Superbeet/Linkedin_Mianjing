import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return None
        
        heap = []
        heapq.heapify(heap) 
        
        size = 0
        for num in nums:
            if size < k:
                heapq.heappush(heap, num)
                size += 1
            elif num > heap[0]:
                heapq.heapreplace(heap, num)
        
        return heapq.heappop(heap)

import random

class Solution:
    def findKthLargest(self, nums, k):
        pivot = random.choice(nums)
        nums1, nums2 = [], []
        for num in nums:
            if num > pivot:
                nums1.append(num)
            elif num < pivot:
                nums2.append(num)
        if k <= len(nums1):
            return self.findKthLargest(nums1, k)
        if k > len(nums) - len(nums2):
            return self.findKthLargest(nums2, k - (len(nums) - len(nums2)))
        return pivot

#通用模板
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return None
        
        return self.quick_select(nums, 0, len(nums)-1, k)
        
    def quick_select(self, nums, left, right, k):
        if left>=right:
            return nums[left]
        
        index = self.partition(nums, left, right)
        # print index
        
        size = index - left + 1
        
        if size == k:
            return nums[index]
        elif size > k:
            return self.quick_select(nums, left, index-1, k)
        else:
            return self.quick_select(nums, index+1, right, k-size)
    
    def partition(self, nums, left, right):
        i, j = left, right
            
        pivot = nums[i]
        
        while i<j:
            while i<j and nums[j]<=pivot:
                j -= 1
            nums[i] = nums[j]
            
            while i<j and nums[i]>=pivot:
                i += 1
            nums[j] = nums[i]

        nums[i] = pivot
        
        return i

# sol = Solution()
# print sol.findKthLargest([1,5,3,6,4,7,2,8], 3)
"""
K largest elements
"""
class Solution(object):
    def findKLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return None
        
        return self.quick_select(nums, 0, len(nums)-1, k)
        
    def quick_select(self, nums, left, right, k):
        if left>=right:
            return [nums[left]]
        
        index = self.partition(nums, left, right)
        # print index
        
        size = index - left + 1
        
        if size == k:
            return nums[left:index+1]
        elif size > k:
            return self.quick_select(nums, left, index-1, k)
        else:
            return nums[left:index+1] + self.quick_select(nums, index+1, right, k-size)
    
    def partition(self, nums, left, right):
        i, j = left, right
            
        pivot = nums[i]
        
        while i<j:
            while i<j and nums[j]<=pivot:
                j -= 1
            nums[i] = nums[j]
            
            while i<j and nums[i]>=pivot:
                i += 1
            nums[j] = nums[i]

        nums[i] = pivot
        
        return i

sol = Solution()
print sol.findKLargest([1,5,3,6,4,7,2,8], 6)