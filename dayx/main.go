package main

import (
	"os"
	"strings"
)

type coordinate struct {
	x int
	y int
}

func TotalResultA(str string) int {
	return 0
}

func TotalResultB(str string) int {
	return 0
}

func Helper1(str string) int {
	return 0
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
	string := GetDataDay()
	println("Result part 1: ", TotalResultA(string))
	println("Result part 2: ", TotalResultB(string))
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func GetDataDay() string {
	dat, err := os.ReadFile("input")
	check(err)
	return string(dat)
}
