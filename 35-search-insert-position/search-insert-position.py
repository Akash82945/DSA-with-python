class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            # Using (low + high) // 2 is fine in Python as integers 
            # don't overflow like in Java or C++.
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        # If not found, 'low' will be the insertion point
        return low
        