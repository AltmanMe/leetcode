class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.length = len(s)
        res = ''
        for i in range(self.length):
            s1 = self.expandAroundcenter(s,i,i)
            if len(s1) > len(res):
                res = s1
            s2 = self.expandAroundcenter(s,i,i+1)
            if len(s2) > len(res):
                res = s2
        return res        
            
    def expandAroundcenter(self,s,l,r):
        left = l
        right = r
        while left >= 0 and right < self.length and s[left] == s[right]:
            left = left - 1
            right = right + 1
        return s[left+1:right]

"""
bruteforce version run time complexity O(n3)
def longestPalindrome(s):
    length = len(s)
    max_len = 0
    left = 0
    right = 1
    for i in range(length-1):
        for j in range(i+1,length):
            if s[i:j+1] == s[i:j+1][::-1]:
                if len(s[i:j+1]) > max_len:
                    max_len = len(s[i:j+1])
                    left = i
                    right = left + max_len
    return s[left:right]

Notice: 
    str = 'abcdefg'
    str[0:len(str)] is the whole string
    slice is left closed and right open
"""
