func sum(nums *[]int) int {
	s := 0
	for _, v := range *nums {
		s += v
	}
	return s
}


func pivotIndex(nums []int) int {
	lsum := 0
	rsum := sum(&nums)
	for i := 0; i < len(nums); i++ {
		t := nums[i]
		rsum = rsum - t
		if rsum == lsum {
			return i
		}
		lsum = lsum + t
	}
	return -1
}
