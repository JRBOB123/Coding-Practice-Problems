class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        i = len(s)-1
        word = ""
        while i >= 0:
            if s[i] != " ":
                word += s[i]
            elif s[i] == " " and word != "":
                return len(word)
            i -= 1
        return len(word)
S1 = Solution()
print(S1.lengthOfLastWord("a"))