class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # k tracks the count and position of elements not equal to val
        k = 0
        
        for i in range(len(nums)):
            # If the current element is NOT the one we want to remove
            if nums[i] != val:
                # Move it to the k-th position
                nums[k] = nums[i]
                # Increment k to prepare for the next valid element
                k += 1
                
        return k