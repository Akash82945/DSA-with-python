class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 1. Create a map of closing brackets to their matching opening brackets
        bracket_map = {")": "(", "}": "{", "]": "["}
        
        # 2. Initialize an empty list to act as our stack
        stack = []
        
        # 3. Loop through every character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element if stack isn't empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the opening bracket matches the required one
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)
        
        # 4. If the stack is empty, all brackets were matched correctly
        return not stack