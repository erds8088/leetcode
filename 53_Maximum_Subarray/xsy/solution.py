class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = nums[0]
        current = -1
        for i in nums:
            if current < 0:
                current = i
            else:
                current += i
            if current > max:
                max = current
        return max 
        