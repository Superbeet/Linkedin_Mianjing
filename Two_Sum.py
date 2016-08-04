"""
Given an array of integers, find two numbers such that they add up to a specific target number.
"""   
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        size = len(nums)
        hashmap = {}
        
        for i in xrange(size):
            num = nums[i]
            
            if target-num in hashmap:
                return [hashmap[target-num], i]
            
            if num not in hashmap:
                hashmap[num] = i
        
        return False
            

"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
"""   
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if numbers is None:
            return [-1, -1]
        
        start, end = 0, len(numbers)-1
        
        while start<end:
            sum = numbers[start] + numbers[end]
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            else:
                return [start+1, end+1]
        
        return [-1, -1]


class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.nums = []
        self.hashmap = {}
    """
    O(1)
    """
    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.nums.append(number)
        if number not in self.hashmap:
            self.hashmap[number] = 1
        else:
            self.hashmap[number] += 1

    """
    O(N)
    """
    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        size = len(self.nums)
        for i in xrange(size):
            num = self.nums[i]
            if value - num in self.hashmap:
                if value - num == num:
                    if self.hashmap[num] >= 2:
                        return True
                else:
                    return True
                    
        return False
        

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)