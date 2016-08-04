class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        target_map = {}
        found_map = {}
        
        for c in t:
            if c not in target_map:
                target_map[c] = 1
                found_map[c] = 0
            else:
                target_map[c] += 1
        
        print "target_map->", target_map
        print "found_map ->", found_map

        min_begin, min_end = -1, len(s)
        begin, end = 0, 0
        count = 0
        
        for end in xrange(0, len(s)):
            # print [begin, end], "min->", [min_begin, min_end]
            
            if s[end] in target_map:

                found_map[s[end]] += 1

                if found_map[s[end]] <= target_map[s[end]]:
                    count += 1
                
                if count == len(t):
                    while (s[begin] not in found_map) or found_map[s[begin]]>target_map[s[begin]]:
                        if (s[begin] in target_map) and found_map[s[begin]]>target_map[s[begin]]:
                            found_map[s[begin]] -= 1
                        begin += 1

                    if end - begin < min_end - min_begin:
                        min_begin = begin
                        min_end = end
        
        result = ( s[min_begin: min_end+1] if min_begin != -1 else "" )
        
        return result

# sol = Solution()
# print sol.minWindow("ADOBECODEBANC", "ABC")
                    
                    


# Using Mapping Array
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        target_map = [0 for i in xrange(256)]
        found_map = [0 for i in xrange(256)]
        
        for c in t:
            target_map[ord(c)] += 1
        
        min_begin, min_end = -1, len(s)
        begin, end = 0, 0
        count = 0
        
        for end in xrange(0, len(s)):
            
            char_end = s[end]
            
            if target_map[ord(char_end)] > 0:    #if it is a char we are looking at
            
                found_map[ord(char_end)] += 1
                
                if found_map[ord(char_end)] <= target_map[ord(char_end)]:
                    count += 1
                    
                if count == len(t):
                    
                    while target_map[ord(s[begin])] == 0 \
                        or found_map[ord(s[begin])] > target_map[ord(s[begin])]:
                        
                        if target_map[ord(s[begin])] > 0 \
                            and found_map[ord(s[begin])] > target_map[ord(s[begin])]:
                            
                            found_map[ord(s[begin])] -= 1
                        
                        begin += 1
                    
                    if end - begin < min_end - min_begin:
                        min_end = end
                        min_begin = begin
        
        result = ( s[min_begin: min_end+1] if min_begin != -1 else "" )
        
        return result
                    
sol = Solution()
print sol.minWindow("ADOBECODEBANC", "ABC")
                    
                    
