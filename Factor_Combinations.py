import math

class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        if n <= 1:
            return res
        self.get_factors(res, [], n, 2)
        return res
    
    def get_factors(self, res, comb, n, start):
        if n == 1:
            if len(comb)>1:
                res.append(copy.deepcopy(comb))
            return
        
        for i in xrange(start, n+1):
            if n % i == 0:
                comb.append(i)
                self.get_factors(res, comb, n/i, i)
                comb.pop()
                