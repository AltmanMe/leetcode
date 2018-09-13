"""
Sort by row
Time complexity: O(n), where n == len(s)
Space complexity: O(n)
"""

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = [[] for i in range(numRows)]
        go_down = False
        n = len(s)
        cur_line = 0
        res = ''
        if numRows == 1:
            return s
        for char in s:
            rows[cur_line].append(char)
            if cur_line == 0 or cur_line == numRows - 1: go_down = not go_down
            if go_down: cur_line = cur_line + 1       
            else: cur_line = cur_line - 1    
        for row in range(numRows):
            res = res + ''.join(rows[row])        
        return res    

"""
initialize a 2D array
[ [] for i in range(num_rows)]
"""
