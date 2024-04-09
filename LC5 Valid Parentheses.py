class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list = []
        i = 0

        while i < len(s):
            if s[i] in ['{', '(', '[']:
                list.append(s[i])
            else:
                if len(list) == 0 : return False
                elif s[i] == '}' and not list.pop() == '{'  : return False
                elif s[i] == ')' and not list.pop() == '(' : return False
                elif s[i] == ']' and not list.pop() == '[' : return False
            i += 1

        return len(list) == 0
