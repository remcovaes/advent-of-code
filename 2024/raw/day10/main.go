package main

import (
	"os"
	"strings"
)

type SingleInput struct {
	single string
}

type PuzzleInput struct {
	lines []SingleInput
}

func parseInput(str string) PuzzleInput {
	sanitized := strings.Trim(str, "\n\t ")
	input := PuzzleInput{}
	for _, item := range strings.Split(sanitized, "\n") {
		if item == "" {
			continue
		}
		singleInput := SingleInput{single: item}

		input.lines = append(input.lines, singleInput)
	}
	return input
}

func TotalResultA(str string) int {
	input := parseInput(str)
	result := HelperPart1(input)
	return result
}

func TotalResultB(str string) int {
	input := parseInput(str)
	result := HelperPart2(input)
	return result
}

func HelperPart1(input PuzzleInput) int {
	total := 0
	for _, line := range input.lines {
		total = HelperSinglePart1(line)
	}
	return total
}

func HelperSinglePart1(line SingleInput) int {
	return 0
}

func HelperPart2(input PuzzleInput) int {
	total := 0
	for _, line := range input.lines {
		total = HelperSinglePart1(line)
	}
	return total
}

func HelperSinglePart2(line SingleInput) int {
	return 0
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
