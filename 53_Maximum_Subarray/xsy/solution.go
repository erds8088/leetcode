func maxSubArray(nums []int) int {
    max := nums[0]
    current := -1
    for _, i := range nums {
        if current < 0 {
            current = i
        } else {
            current += i
        }
        if current > max {
            max = current
        }
    }
    return max
}