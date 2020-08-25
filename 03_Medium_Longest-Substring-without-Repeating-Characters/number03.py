# Runtime: 140 ms, faster than 25.37% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.1 MB, less than 19.28% of Python3 online submissions for Longest Substring Without Repeating Characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestLength = 0
        substring = []
        
        for current in s:
            substring.append(current)
            
            if substring.count(current) == 2:
                firstOccurrence = substring.index(current) + 1
                substring = substring[firstOccurrence:]
            
            if len(substring) > longestLength:
                longestLength = len(substring)
            
        return longestLength
