package _1

// twoSum遍历
func twoSum(nums []int, target int) []int {
    for i := 0; i<len(nums)-1; i++ {
        for j := i+1; j<len(nums); j++ {
            if nums[i] + nums[j] == target {
                return []int{i, j}
            }
        }
    }
    return []int{}   
}

// twoSum2使用map存储
func twoSum2(nums []int, target int) []int {
    m := map[int]int{}
    for i, v := range nums {
        if j, ok := m[v]; ok {
            return []int{j, i}
        } else {
            m[target-v] = i
        }
    }
    return []int{}
}