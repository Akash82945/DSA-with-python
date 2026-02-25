class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        # Traverse the array from the end (least significant digit)
        for i in range(n - 1, -1, -1):
            # If the digit is less than 9, just increment and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If the digit is 9, it becomes 0 and the loop carries over
            digits[i] = 0
            
        # If we finished the loop, it means all digits were 9
        # Example: [9, 9] became [0, 0], so we need to add 1 at the front
        return [1] + digits