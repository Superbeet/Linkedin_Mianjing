class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        
        if nestedList is None:
            return 0
        
        stack = []
        
        for item in nestedList:
            stack.append( (item,1) )
        
        sum = 0
        
        while stack:
            next, d = stack.pop()
            if next.isInteger():
                sum += d * next.getInteger()
            else:
                for item in next.getList():
                    stack.append( (item, d+1) )
        
        return sum

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        
        if nestedList is None:
            return 0
        
        return self.getSum(nestedList, 1)
    
    def getSum(self, items, depth):
        sum = 0
        for item in items:
            if item.isInteger():
                sum += depth*item.getInteger()
            else:
                sum += self.getSum(item.getList(), depth+1)
        
        return sum


class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if nestedList is None or len(nestedList) == 0:
            return 0

        max_depth = self.maxDepth(nestedList, 1)
        return self.getSum(nestedList, max_depth)
    
    # Key Points
    def maxDepth(self, nestedList, depth):
        if not nestedList:
            return 0
            
        max_depth = depth
        for item in nestedList:
            if not item.isInteger():
                max_depth = max(max_depth, self.maxDepth(item.getList(), depth + 1))
                
        return max_depth
    
    def getSum(self, nestedList, depth):
        sum = 0
        for item in nestedList:
            if item.isInteger():
                sum += item.getInteger() * depth
            else:
                sum += self.getSum(item.getList(), depth - 1)
        return sum
        
        
void DFS(vector<NestedInteger>& nestedList, int depth)
    {
        maxDepth = max(maxDepth, depth);
        for(auto val: nestedList)
        {
            if(!val.isInteger()) 
                DFS(val.getList(), depth+1); 
            else 
                nums.push_back(make_pair(val.getInteger(), depth));
        }
    }
    
    int depthSumInverse(vector<NestedInteger>& nestedList) {
        if(nestedList.size() ==0) 
            return 0;
        DFS(nestedList, 1);

        for(auto val: nums) 
            result+= (maxDepth-val.second+1)*val.first;

        return result;
    }
private:
    vector<pair<int, int>> nums;
    int maxDepth = 0, result = 0;