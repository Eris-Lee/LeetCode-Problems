class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        needle_size = len(needle)
        #window = haystack[:needle_size]
        if (len(haystack) == needle_size) and haystack == needle:
            return 0
        
        if needle_size == 1:
            for i in range(len(haystack)):
                if haystack[i] == needle:
                    return i
                print(haystack[i])
        
        else:
            for i in range((len(haystack)-len(needle))+1):
                window = haystack[i:i+needle_size]
                if window == needle:
                    return i
        return -1
        