class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        track_list = []
        reverse_list = []

        #Append gradually to the stack
        track_list.append(s[0])
        reverse_list.append(0)
        for i in range(1, len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                track_list.append(s[i])
                reverse_list.append(i)
            if s[i] == ")":
                if len(track_list) == 0:
                    return False
                a = track_list.pop()
                if a != "(":
                    return False
            if s[i] == "]":
                if len(track_list) == 0:
                    return False
                a = track_list.pop()
                if a != "[":
                    return False
            if s[i] == "}":
                if len(track_list) == 0:
                    return False
                a = track_list.pop()
                if a != "{":
                    return False
        if len(track_list) != 0:
            return False
        else:
            return True
