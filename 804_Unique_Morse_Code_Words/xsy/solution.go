func uniqueMorseRepresentations(words []string) int {
    morse := []string{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."}
	codes := map[string]int{}
	for _, word := range words {
		temp := ""
		for _, w := range word {
			temp += morse[rune(w)-97]
		}
		codes[temp] += 1
	}
	return len(codes)
}
