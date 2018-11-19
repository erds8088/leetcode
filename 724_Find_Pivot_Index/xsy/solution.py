class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lsum =  0
        rsum = sum(nums)
        for i in range(len(nums)):
            t = nums[i]
            rsum -= t
            if lsum == rsum:
                return i
            lsum += t
        return -1