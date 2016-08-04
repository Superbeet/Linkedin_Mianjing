import copy

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if not nums:
            return []
        
        result = []
        visited = set([])
        self.helper(nums, visited, [], result)
        return result
        
    def helper(self, nums, visited, perm, res):
        if len(visited) == len(nums):
            res.append(copy.deepcopy(perm))
            return
        
        for i in xrange(len(nums)):
            if nums[i] in visited:
                continue
            
            perm.append(nums[i])
            visited.add(nums[i])
            self.helper(nums, visited, perm, res)
            visited.remove(nums[i])
            perm.pop()
        
        return

import copy

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        visited = [0 for i in xrange(len(nums))]
        result = []
        nums = sorted(nums)
        self.helper(nums, visited, [], result)
        return result
    
    def helper(self, nums, visited, perm, res):
        if len(perm) == len(nums):
            res.append(copy.deepcopy(perm))
            return
        
        for i in xrange(len(nums)):
            # Keep duplicated elements access order, if duplicated elements are visited 
            # out of order. Stop the recursion.
            if visited[i]==1 or ( i>0 and nums[i]==nums[i-1] and visited[i-1]==0):
                continue
            
            visited[i] = 1
            perm.append(nums[i])
            self.helper(nums, visited, perm, res)
            perm.pop()
            visited[i] = 0
