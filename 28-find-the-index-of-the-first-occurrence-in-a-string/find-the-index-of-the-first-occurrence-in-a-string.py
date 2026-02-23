class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n, m = len(haystack), len(needle)
        
        # If the needle is empty, the first occurrence is at index 0
        if m == 0:
            return 0
        
        # We only need to iterate up to the point where needle can still fit
        for i in range(n - m + 1):
            # Check character by character
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    break
                # If we reached the end of the needle without a mismatch
                if j == m - 1:
                    return i
                    
        return -1