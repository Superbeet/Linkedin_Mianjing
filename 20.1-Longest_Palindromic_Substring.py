"""
DP
Time = O(n^2)
Space = O(n^2)
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        
        dp = [[False for i in range(size)] for i in range(size)]
        
        longest_begin = 0 
        longest_leng = 1
        
        for i in xrange(size):
            dp[i][i] = True
        
        for i in xrange(size-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                longest_begin = i
                longest_leng = 2
        
        for leng in xrange(2, size+1):
            for i in xrange(0, size-leng+1):
                j = i + leng -1
                
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    longest_begin = i
                    longest_leng = leng
        
        return s[longest_begin:longest_begin+longest_leng]

sol = Solution()
s = "GEEKS FOR GEEKS"
print sol.longestPalindrome(s)

