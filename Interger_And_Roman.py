class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num <= 0:
            return ""
        
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        res = ""
        digit = 0
        
        while num > 0:
            times = num / nums[digit]
            num -= nums[digit]*times
            res += symbols[digit]*times
            digit += 1
        
        return res
            
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        map = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        
        res = map[s[-1]]
        size = len(s)
        
        for i in xrange(size-2, -1, -1):
            roman = map[s[i]]
            if roman<map[s[i+1]]:
                res -= roman
            else:
                res += roman
        
        return res
            
        