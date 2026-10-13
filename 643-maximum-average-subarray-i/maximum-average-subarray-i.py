class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_avg = float(sum(nums[:k]))
        max_avg = window_avg/k
        for i in range(len(nums)-k):
            window_avg = window_avg - nums[i] + nums[i+k]
            max_avg = max(max_avg, window_avg/k)
        return max_avg
        