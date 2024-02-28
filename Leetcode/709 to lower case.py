class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_string = ""
        for i in range(len(s)):
            if ord(s[i]) >=65 and ord(s[i]) <=90:
                new_string += chr(ord(s[i]) + 32)
            else:
                new_string += s[i]


        return new_string

S1 =Solution()
print(S1.toLowerCase("Hello"))
