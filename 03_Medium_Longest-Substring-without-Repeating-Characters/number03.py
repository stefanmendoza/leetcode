# Runtime: 168 ms, faster than 22.39% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14 MB, less than 35.57% of Python3 online submissions for Longest Substring Without Repeating Characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestLength = 0
        priorSubstring = []
        substring = []
        
        for current in s:
            priorSubstring = substring
            substring.append(current)
            
            if substring.count(current) == 2:
                firstOccurrence = substring.index(current) + 1
                substring = substring[firstOccurrence:]
            
            if len(substring) > longestLength:
                longestLength = len(substring)
            
        return longestLength