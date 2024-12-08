package main

import (
	"os"
	"strings"
)

type SinlgeInput struct {
	single string
}

type PuzzleInput struct {
	lines []SinlgeInput
}

func parseInput(str string) PuzzleInput {
	input := PuzzleInput{}
	for _, item := range strings.Split(str, "\n") {
		if item == "" {
			continue
		}
		singleInput := SinlgeInput{single: item}
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

func HelperSinglePart1(line SinlgeInput) int {
	return 0
}

func HelperPart2(input PuzzleInput) int {
	total := 0
	for _, line := range input.lines {
		total = HelperSinglePart1(line)
	}
	return total
}

func HelperSinglePart2(line SinlgeInput) int {
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
