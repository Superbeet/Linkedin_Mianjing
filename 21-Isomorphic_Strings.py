class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None:
        	return False

        elif len(s)!=len(t):
            return False
        
        elif len(s) < 2:
        	return True

        size = len(s)
        hashmap = {}
        hashrev = {}
        for i in xrange(size):
            if s[i] not in hashmap:
                hashmap[s[i]] = t[i]
            else:
                if hashmap[s[i]] != t[i]:
                    return False
            
            if t[i] not in hashrev:
                hashrev[t[i]] = s[i]
            else:
                if hashrev[t[i]] != s[i]:
                    return False
        
        return True
            
        