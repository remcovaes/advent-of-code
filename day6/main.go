package main

import (
	"os"
	"strings"
)

func TotalResultA(str string) int {
	return 0
}

func TotalResultB(str string) int {
	return 0
}

func Helper1(str string) bool {
	return false
}

func Helper2(str string) int {
	return 0
}

func Helper3(str string) int {
	return 0
}

func splitIntoNewlines(str string) []string {
	return strings.Split(str, "\n")
}

func main() {
	string := getDataDay()
	println("Result part 1: ", TotalResultA(string))
	println("Result part 2: ", TotalResultB(string))
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func getDataDay() string {
	dat, err := os.ReadFile("input")
	check(err)
	return string(dat)
}
