class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers)-1
        added = numbers[l]+numbers[r]
        #print(added)
        while l < r:
            if added == target:
                #print("all done")
                return [l+1, r+1]
            if added < target:
                l+=1
            else:
                r-=1
            added = numbers[l]+numbers[r]
            #print(added)
        return [l+1, r+1]  