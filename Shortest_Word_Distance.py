import sys
"""
Shortest Word Distance 1
"""
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index1, index2 = -1, -1
        min_dist = sys.maxint
        for i in xrange(len(words)):
            if words[i] == word1:
                index1 = i
            elif words[i] == word2:
                index2 = i
            
            if index1 != -1 and index2 != -1:
                min_dist = min(min_dist, abs(index2-index1))
        
        return min_dist

"""
Shortest Word Distance 2
Same words allowed - We cannot update two indices at once.
"""
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index1, index2 = -1, -1
        turn = False
        min_dist = sys.maxint
        for i in xrange(len(words)):
            if words[i] == word1:
                index1 = i
            elif words[i] == word2:
                index2 = i
                
            if index1 != -1 and index2 != -1 and index1 != index2:
                min_dist = min(min_dist, abs(index2-index1))
            
            if word1 == word2:
                index2 = index1
            
        return min_dist

"""
Shortest Word Distance II
Class and repeatly calling
"""
class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        if words is None:
            raise Exception("Invalid None Value")
            return
        
        self.hashmap = {}
        
        for i, word in enumerate(words):
            if word not in self.hashmap:
                self.hashmap[word] = [i]
            else:
                self.hashmap[word].append(i)
            
    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        list1 = self.hashmap[word1]
        list2 = self.hashmap[word2]
        
        i, j = 0, 0
        
        min_dist = sys.maxint
        
        while i<len(list1) and j<len(list2):
            dist = abs(list1[i]-list2[j])
            min_dist = min(min_dist, dist)
            
            if list1[i] < list2[j]:
                i += 1
            
            else:
                j += 1
        
        return min_dist

