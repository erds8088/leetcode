package main

import (
	"strconv"
	"fmt"
)

func fizzBuzz(n int) []string {
    s := []string{}
    tree := 0
    five := 0
    for i := 1; i<=n; i++ {
        tree += 1
        five += 1
        var t string
        if tree == 3 {
            t += "Fizz"
            tree = 0
        } 
        if five == 5 {
            t += "Buzz";
            five = 0
        } 
        if t == "" {
            t = strconv.Itoa(i)
        }
        s = append(s, t)
    }
    return s
}


func main() {
    fmt.Println(fizzBuzz(15))
}
