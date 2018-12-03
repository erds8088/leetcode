class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = dict()
        for index, num in enumerate(nums):
            if num in m:
                return [m[num], index]
            else:
                m[target-num] = index
        return []
