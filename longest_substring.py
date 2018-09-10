"""
Longest Substring Without Repeating Characters
"""

def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    left = 0
    dic = dict()
    result = 0
    for right, char in enumerate(s):
        if char in dic:
            left = max(left, dic[char] + 1)
        dic[char] = right
        result = max(result, right - left + 1)
    return result

"""
for line 15:
if left = dic[char] + 1 instead of above code
when the input is abba
the position of left pointer would be wrong
"""
