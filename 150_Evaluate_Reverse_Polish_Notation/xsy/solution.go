func evalRPN(tokens []string) int {
	operations := map[string]func(int, int) int{
		"+": func(number1, number2 int) int {return number1+number2},
		"-": func(number1, number2 int) int {return number1-number2},
		"*": func(number1, number2 int) int {return number1*number2},
		"/": func(number1, number2 int) int {return int(number1/number2)},
	}
	stack := []int{}
	for _, token := range tokens {
		if operationfunc, had := operations[token]; had {
			length := len(stack)
			number1, number2 := stack[length-2], stack[length-1]
			stack = stack[:length-2]
			number := operationfunc(number1, number2)
			stack = append(stack, number)
		} else {
			number, _ := strconv.Atoi(token)
			stack = append(stack, number)
		}
	}
	return stack[0]
}
