class Solution:
    def permute(self, nums):
        """
        可以转化成求nums[1:]的组合，然后将nums[0]插入到nums[1:]的所有组合中
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        
        result = []
        perms = self.permute(nums[1:])
        for perm in perms:
            for i in range(len(perm)+1):
                p = perm[:i] + nums[:1] + perm[i:]
                result.append(p)
        return result
