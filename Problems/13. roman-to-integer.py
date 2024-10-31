class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result=0
        for i in range(len(s)):
            value=roman[s[i]]
            if i<len(s)-1 and value < roman[s[i+1]]:
                result = result - value
            else:
                result = result + value
        return result
