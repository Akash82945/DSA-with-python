class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # 'i' is the index of the last unique element found
        i = 0
        
        # 'j' scans the rest of the array
        for j in range(1, len(nums)):
            # If we find a new unique value
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        # The number of unique elements is index + 1
        return i + 1