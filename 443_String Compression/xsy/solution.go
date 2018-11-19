func compress(chars []byte) int {
    count := 1
    k := 0
    length := len(chars)
    for i := 0; i < length; i++ {
        if i+1 >= length || chars[i+1] != chars[i] {
            k ++
            if count > 1 {
                count_str := strconv.Itoa(count)
                for _, c := range count_str {
                    chars[k] = byte(c)
                    k++
                }
            }
            if i+1 < length {
                chars[k] = chars[i+1]
                count = 1
            }
        } else {
            count ++
        }
    }
    return k
}
