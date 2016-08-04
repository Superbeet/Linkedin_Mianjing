"""
General recursive solution
Time O(2^n)
"""
class Solution(object):
    def longestPalindromeSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.lps(s, 0, len(s)-1)

    def lps(self, s, start, end):
    	if start >= end:
    		return 1

    	if s[start] == s[end] and start + 1 == end:
    		return 2

    	if s[start] == s[end]:
    		return self.lps(s, start + 1, end - 1) + 2

    	else:
    		return max(self.lps(s, start + 1, end), self.lps(s, start, end - 1))


# sol = Solution()
# s = "GEEKSFORGEEKS"
# print sol.longestPalindromeSubsequence(s)

"""
DP
Time = O(n^2)
Space = O(n^2)
"""
class Solution(object):
    def longestPalindromeSubsequence(self, s):
    	size = len(s)

    	dp = [[0 for i in xrange(size)] for j in xrange(size)]

    	for i in xrange(size):
    		dp[i][i] = 1

    	for cl in xrange(2, size+1):
    		for i in xrange(0, size-cl+1): # Open Interval
    			j = i + cl -1

    			if s[i] == s[j] and i + 1 == j:
    				pass
    				# dp[i][j] = 2

    			elif s[i] == s[j]:
    				dp[i][j] = dp[i+1][j-1] + 2

    			else:
    				dp[i][j] = max(dp[i][j-1], dp[i+1][j])

    	return dp[0][size-1]


sol = Solution()
s = "GEEKS FOR GEEKS"
print sol.longestPalindromeSubsequence(s)


"""
1) Reverse the given sequence and store the reverse in another array say rev[0..n-1]
2) LCS of the given sequence and rev[] will be the longest palindromic sequence.
This solution is also a O(n^2) solution.
"""