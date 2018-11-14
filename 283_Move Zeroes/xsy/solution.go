func moveZeroes(nums []int)  {
    end := len(nums)
    slow_ptr := 0
    for fast_ptr := 0; fast_ptr < end; fast_ptr++ {
        if nums[fast_ptr] == 0 {
            continue
        }
        if fast_ptr != slow_ptr {
            nums[fast_ptr], nums[slow_ptr] = nums[slow_ptr], nums[fast_ptr]
        }
        slow_ptr ++
    }
}
