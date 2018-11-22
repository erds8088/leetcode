package main


func scoreOfParentheses(S string) int {
	count := 0
	status := false
	ans := 0
	for _, s := range S {
		if s == '(' {
			count += 1
			status = true
		} else {
			count -= 1
			if status {
				ans += pow(2, count*1)
				status = false
			}
		}
	}
	return ans
}


func pow(x, n int) int {
	var r int = 1
	if x == 0 {
		return 0
	}
	if n == 0 {
		return 1
	}
	for i := 1; i <= n; i++ {
		r = r * x
	}
	return r
}


func main() {
	scoreOfParentheses("(()((())))")
}