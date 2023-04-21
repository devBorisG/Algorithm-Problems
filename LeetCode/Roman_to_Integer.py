class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        for item in range(len(s)):
            if item+1 < len(s)  and roman[s[item]] < roman[s[item+1]]:
                result -= roman[s[item]]
            else:
                result += roman[s[item]]
        return result