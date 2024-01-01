class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        word_list = []
        word = ""
        for i in range(len(s)):
            if s[i] != " ":
                word += s[i]

            if i >= 1:
                if (s[i] == " " and s[i - 1] != " "):
                    word_list.append(word)
                    word = ""

        if s[len(s) - 1] != " ":
            word_list.append(word)

        reverse_string = ""
        for j in range(len(word_list)-1, 0, -1):
            reverse_string += word_list[j] + " "

        reverse_string += word_list[0]
        return reverse_string


r1 = Solution()
print(r1.reverseWords("  hello world  "))
print(r1.reverseWords("the sky is blue"))
print(r1.reverseWords("a good   example"))
