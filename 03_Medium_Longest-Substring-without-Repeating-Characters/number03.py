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


########################
#   Optimal Solution   #
########################


# This solution uses a "sliding window" hash set. Let me know if you have any questions!
# 
# Detailed explanation:
# 
# left and right are indexes into the string. These bound the current substring we're looking at.
# We also have a hash set, chars, which stores the characters in the current substring.
# 
# Both indices start at 0. We check if string[right] is in our hash set of current characters;
# if it isn't, it's a unique character we can add to the current substring.
# So, we add it to the set of characters, and increment right.
# We also potentially update longest with the length of the current substring.
# 
# If string[right] is in the hash set of characters, we remove string[left] from the hash set,
# and increment left. This is because the character at right is a duplicate of some character
# in the substring; we want to keep removing the leftmost character from the current substring
# until we remove that character. Then, since we have another candidate for longest non-repeating
# substring, we can enter the if block, and go back to incrementing right.
# 
# By the time the while loop terminates, we've considered every substring with unique characters,
# and we know the length of the longest. left and right were incremented linearly through the string,
# and the hash set allowed for O(1) lookups, so the time complexity is O(n).

class Solution:

    def lengthOfLongestSubstring(self, string):
        """
        Time:  O(n)
        Space: O(k)
        [k = length of the longest substring w/o repeating characters]
        """
        longest = 0
        left, right = 0, 0
        chars = set()
        while left < len(string) and right < len(string):
            if string[right] not in chars:
                chars.add(string[right])
                right += 1
                longest = max(longest, right - left)
            else:
                chars.remove(string[left])
                left += 1
        return longest