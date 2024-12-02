package main

import (
	"os"
	"slices"
	"strconv"
	"strings"
)

func TotalResultA(str string) int {
	total := 0
	splitDoubleNew := strings.Split(str, "\n\n")
	rules := ParseRules(splitDoubleNew[0])

	for _, line := range splitIntoNewlines(splitDoubleNew[1]) {
		total += Helper2(rules, stringsToInts(line, ","))
	}
	return total
}

func TotalResultB(str string) int {
	total := 0
	splitDoubleNew := strings.Split(str, "\n\n")
	rules := ParseRules(splitDoubleNew[0])

	for _, line := range splitIntoNewlines(splitDoubleNew[1]) {
		ints := []int{}
		for _, letter := range strings.Split(line, ",") {
			num, _ := strconv.Atoi(letter)
			ints = append(ints, num)
		}

		total += Helper3(rules, ints)
	}
	return total
}

func ParseRules(str string) map[int][]int {
	result := make(map[int][]int)
	lines := splitIntoNewlines(str)
	for _, line := range lines {
		split := strings.Split(line, "|")
		numStr1, _ := strconv.Atoi(split[1])
		numStr2, _ := strconv.Atoi(split[0])
		_, exists := result[numStr1]
		if !exists {
			result[numStr1] = []int{numStr2}
			continue
		}
		result[numStr1] = append(result[numStr1], numStr2)
	}

	return result
}

func Helper2(rules map[int][]int, nums []int) int {
	for index, num := range nums {
		rule, exists := rules[num]
		if !exists {
			continue
		}
		currentSlice := nums[:index]
		for _, item := range rule {
			if !slices.Contains(currentSlice, item) {
				if slices.Contains(nums, item) {
					return 0
				}
			}
		}
	}
	return nums[(len(nums)-1)/2]
}

func Helper3(rules map[int][]int, nums []int) int {
	result := Helper2(rules, nums)
	if result != 0 {
		return 0
	}
	newArr := CorrectArray(rules, nums)
	return newArr[(len(newArr)-1)/2]
}

func CorrectArray(rules map[int][]int, nums []int) []int {
	for index, num := range nums {
		rule, exists := rules[num]
		if !exists {
			continue
		}
		currentSlice := nums[:index]
		for _, item := range rule {
			if slices.Contains(currentSlice, item) {
				continue
			}
			if !slices.Contains(nums, item) {
				continue
			}
			ruleNumIndex := index
			originalNumIndex := slices.Index(nums, item)
			copySlice := slices.Clone(nums)
			copySlice = slices.Replace(copySlice, ruleNumIndex, ruleNumIndex+1, item)
			copySlice = slices.Replace(copySlice, originalNumIndex, originalNumIndex+1, num)
			return CorrectArray(rules, copySlice)
		}
	}
	return nums
}

func stringsToInts(line string, splitChar string) []int {
	ints := []int{}
	for _, letter := range strings.Split(line, splitChar) {
		num, _ := strconv.Atoi(letter)
		ints = append(ints, num)
	}
	return ints
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
