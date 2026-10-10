class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        best = 0
        while l < r:
            h = min(height[l], height[r]) #gives the lesser between the two
            area = (r-l)*h
            #print(area)
            if area > best:
                best = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return best