class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([char for char in s if char.isalnum()]).lower()
        reversed = s[::-1]
        if s == reversed:
            return True
        return False
        