class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_letter = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                        "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        seen = {""}
        for i in range(len(words)):
            result = ""
            for j in range(len(words[i])):
                result += (morse_letter[ord(words[i][j]) - ord('a')])
            seen.add(result)


        return len(seen) - 1
