# Runtime: 88 ms
# Your runtime beats 10.63 % of python3 submissions.

# Memory Usage: 14 MB
# Your memory usage beats 12.48 % of python3 submissions.

class Solution:

    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def translate(self, val1: str, val2: str) -> (bool, int):
        if val1 == 'I':
            if val2 == 'V':
                return (True, 4)
            if val2 == 'X':
                return (True, 9)

        if val1 == 'X':
            if val2 == 'L':
                return (True, 40)
            if val2 == 'C':
                return (True, 90)

        if val1 == 'C':
            if val2 == 'D':
                return (True, 400)
            if val2 == 'M':
                return (True, 900)

        return (False, self.values[val1])

    def romanToInt(self, s: str) -> int:
        numericValue = 0

        if len(s) == 1:
            return self.values[s[0]]

        skip = False
        for i in range(0, len(s)):
            if skip:
                skip = False
                continue

            if i == len(s) - 1:
                numericValue += self.values[s[i]]
            else:
                skip, value = self.translate(s[i], s[i+1])
                numericValue += value

        return numericValue
