class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        i = len(s) - 1
        
        # Step 1: Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
            
        # Step 2: Count characters until we hit a space or start of string
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
            
        return length