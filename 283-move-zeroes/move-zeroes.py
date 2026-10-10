class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #use .pop and append
        l, r = 0, len(nums)-1
        while l < r:
            if nums[l] == 0:
                nums.append(0)
                nums.pop(l)
                r-=1
            else:
                l+=1
        return nums
        