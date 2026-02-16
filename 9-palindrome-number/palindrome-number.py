class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Step 1: Handle negatives (Example 2: -121 is never a palindrome)
        if x < 0:
            return False
            
        # Step 2: Convert to string to allow slicing
        x_str = str(x)
        
        # Step 3: Reverse the string using [::-1]
        reversed_x = x_str[::-1]
        
        # Step 4: Compare and return the boolean result
        return x_str == reversed_x