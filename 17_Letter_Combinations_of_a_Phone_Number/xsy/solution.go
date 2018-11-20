func letterCombinations(digits string) []string {
	phone := map[string]string{
		"1": "",     "2": "abc", "3": "def", 
		"4": "ghi",  "5": "jkl", "6": "mno", 
		"7": "pqrs", "8": "tuv", "9": "wxyz",
	}
	result := []string{}
	if len(digits) !=0 {
		result = append(result, "")
	}
	for _, digit := range digits {
		letters, _ := phone[string(digit)]
		new := []string{}
		for _, letter := range letters {
			for _, s := range result {
				new = append(new, s+string(letter))
			}
		}
		result = new
	}
	return result
}
