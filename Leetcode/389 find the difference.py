class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        alphabet_1 = [0] * 26
        alphabet_2 = [0] * 26

        for i in range(len(s)):
            a = ord(s[i]) - ord('a')
            alphabet_1[a] += 1

        for j in range(len(t)):
            a = ord(t[j]) - ord('a')
            if alphabet_2[a] == alphabet_1[a]:
                return t[j]
            else:
                alphabet_2[a] += 1

S1 = Solution()
S1.findTheDifference("a", "aa")