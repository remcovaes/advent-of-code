package main

import (
	"os"
	"regexp"
	"strconv"
	"strings"
)

func TotalResultA(str string) int {
	r := regexp.MustCompile(`mul\(\d+\,\d+\)`)
	splitted := r.FindAllString(str, -1)
	total := 0
	for _, item := range splitted {
		if len(item) == 0 {
			continue
		}
		trimFront := strings.Trim(item, "mul(")
		trimEnd := strings.Trim(trimFront, ")")
		split := strings.Split(trimEnd, ",")
		num1, _ := strconv.Atoi(split[0])
		num2, _ := strconv.Atoi(split[1])
		total = total + num1*num2
	}
	return total
}

func TotalResultB(str string) int {
	r := regexp.MustCompile(`mul\(\d+\,\d+\)`)
	replace := regexp.MustCompile(`(?s)don\'t\(\).*?do\(\)`)
	cleaned := replace.ReplaceAllString(str, "")
	splitted := r.FindAllString(cleaned, -1)
	total := 0
	for _, item := range splitted {
		if len(item) == 0 {
			continue
		}
		trimFront := strings.Trim(item, "mul(")
		trimEnd := strings.Trim(trimFront, ")")
		split := strings.Split(trimEnd, ",")
		num1, _ := strconv.Atoi(split[0])
		num2, _ := strconv.Atoi(split[1])
		total = total + num1*num2
	}
	return total
}

func Helper1(input []int) bool {
	return false
}

func Helper2(input []int) bool {
	return false
}

func Helper3(input []int) bool {
	return false
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
