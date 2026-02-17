class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 1. Handle the case where the list is empty
        if not strs:
            return ""
        
        # 2. Iterate through each character of the first word
        first_word = strs[0]
        for i in range(len(first_word)):
            char = first_word[i]
            
            # 3. Compare this character with the rest of the words
            for other_word in strs[1:]:
                # If 'i' is out of bounds for the other word OR characters don't match
                if i == len(other_word) or other_word[i] != char:
                    # Return the portion of the first word before this index
                    return first_word[:i]
        
        # 4. If we finish the loop, the entire first word is the prefix
        return first_word