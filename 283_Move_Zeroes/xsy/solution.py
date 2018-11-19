class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        slow_ptr = 0
        for fast_ptr in range(length):
            # 跳过0值，将0值交给慢指针处理
            if nums[fast_ptr] == 0:
                continue
            # 如果快指针所指的值非0值，且快慢指针不相等，则交换其值
            if fast_ptr != slow_ptr:
                nums[fast_ptr], nums[slow_ptr] = nums[slow_ptr], nums[fast_ptr]
            slow_ptr += 1
