
def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
     """

    # Determine which word has higher length
    length = 0
    if len(word1) > len(word2):
        length = len(word1)
    else:
        length = len(word2)

     # Append letters together
    merged = ""

    for i in range(length):
        if i < len(word1):
            merged += word1[i]

        if i < len(word2):
            merged += word2[i]

    return merged

print(mergeAlternately("abcd", "pq"))

print(16%7)
