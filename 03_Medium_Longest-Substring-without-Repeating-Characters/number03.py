class Solution:
    seen = {}
    
    def lengthOfLongestSubstring(self, s: str) -> int:        
        longestLength = 0
        currentSubstring = []
        
        for currentChar in s:
            if currentChar in self.seen:            
                currentSubstring = [currentChar]
                self.seen = {}
            else:
                currentSubstring.append(currentChar)
                
                if len(currentSubstring) > longestLength:
                    longestLength = len(currentSubstring)
            
            self.seen[currentChar] = True
                
        return longestLength
