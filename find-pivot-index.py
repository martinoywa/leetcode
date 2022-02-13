class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # sum
        total = sum(nums)
        # left sum
        left_sum = 0
        
        # loop throught the array
        for i in range(len(nums)):
            # check left sum and right sum
            if left_sum == total - nums[i] - left_sum:
                return i
            # increment left sum
            left_sum += nums[i]
        return -1
        
