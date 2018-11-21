func permute(nums []int) [][]int {
    lnums := len(nums)
    if lnums <= 1 {
        return [][]int{nums}
    }
    result := [][]int{}
    perms := permute(nums[:lnums-1])
    for _, perm := range perms {
        end := len(perm)
        for i := 0; i<=end; i++ {
            p := []int{}
            p = append(p, perm[:i]...)
            p = append(p, nums[lnums-1])
            p = append(p, perm[i:]...)
        result = append(result, p)
        }
    }
    return result
}
