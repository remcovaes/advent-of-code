package main

import (
	"math"
	"os"
	"strconv"
	"strings"
)

func TotalResultA(str string) int {
	splitted := splitIntoNewlines(str)

	total := 0
	for _, item := range splitted {
		if len(item) == 0 {
			continue
		}
		parts := strings.Split(item, " ")
		nums := make([]int, 0)
		for _, part := range parts {
			parsed, _ := strconv.Atoi(part)
			nums = append(nums, parsed)
		}
		if IsSafe(nums) {
			total++
		}
	}
	return total
}

func TotalResultB(str string) int {
	splitted := splitIntoNewlines(str)

	total := 0
	for _, item := range splitted {
		if len(item) == 0 {
			continue
		}
		parts := strings.Split(item, " ")
		nums := make([]int, 0)
		for _, part := range parts {
			parsed, _ := strconv.Atoi(part)
			nums = append(nums, parsed)
		}
		if IsSafeB(nums, false) {
			total++
		}
	}
	return total
}
func IsSafeB(input []int, hasBadLevel bool) bool {
	if IsSafe(input) {
		return true
	}

	for index := range input {
		part1 := input[:index]
		part2 := input[index+1:]
		newList := make([]int, 0)
		for _, i := range part1 {
			newList = append(newList, i)
		}
		for _, i := range part2 {
			newList = append(newList, i)
		}

		if IsSafe(newList) {
			return true
		}
	}
	return false
}

func IsSafe(input []int) bool {
	var previous int
	var increasing bool
	for index, item := range input {
		if index == 0 {
			previous = item
			continue
		}
		if index == 1 {
			increasing = item > previous
		}
		if item >= previous && !increasing {
			return false
		}
		if previous >= item && increasing {
			return false
		}
		diff := int(math.Abs(float64(item - previous)))

		if diff > 3 {
			return false
		}

		previous = item
	}
	return true
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
