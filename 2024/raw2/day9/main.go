package main

import (
	"os"
	"strconv"
	"strings"
)

type SingleInput struct {
	id        int
	position  int
	free      int
	size      int
	filled    int
	filleable bool
	origSize  int
}

type PuzzleInput struct {
	lines []SingleInput
}

func parseInput(str string) PuzzleInput {
	sanitized := strings.Trim(str, "\n\t ")
	input := PuzzleInput{}
	position := 0
	strlist := strings.Split(sanitized, "")
	for index := 0; index < (len(strlist)); index += 2 {
		fileSize, _ := strconv.Atoi(strlist[index])
		freeSpaceCurrent := 0
		if len(strlist) > index+1 {
			freeSpaceCurrent, _ = strconv.Atoi(strlist[index+1])
		}
		singleInput := SingleInput{}
		singleInput.id = index / 2
		singleInput.position = position
		singleInput.free = freeSpaceCurrent
		singleInput.size = fileSize
		singleInput.origSize = fileSize
		singleInput.filleable = true

		input.lines = append(input.lines, singleInput)

		position = position + fileSize + freeSpaceCurrent
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

	reversedIndex := len(input.lines) - 1

	lines := input.lines
	for index := range len(lines) {
		current := make([]int, 0)
		for range input.lines[index].size {
			current = append(current, input.lines[index].id)
		}
		input.lines[index].size = 0

		for input.lines[index].free != 0 && reversedIndex >= index {
			if input.lines[index].position > input.lines[reversedIndex].position {
				break
			}
			if input.lines[reversedIndex].size == 0 {
				reversedIndex--
				continue
			}
			for range input.lines[reversedIndex].size {
				current = append(current, input.lines[reversedIndex].id)
				input.lines[reversedIndex].size--
				input.lines[index].free--

				if input.lines[index].free == 0 {
					break
				}
			}
		}
		if input.lines[index].free < 0 {
			panic("can not happen")
		}
		if input.lines[index].size < 0 {
			panic("can not happen")
		}
		for i, final := range current {
			total = total + (input.lines[index].position+i)*final
		}
	}

	return total
}

func HelperSinglePart1(line SingleInput) int {
	return 0
}

func HelperPart2(input PuzzleInput) int {
	xinput := input.lines
	total := 0
	for itemIndex := range xinput {
		item := xinput[itemIndex]
		spaceLeft := item.free - item.filled
		if spaceLeft > 0 {
			// try to find a filler
			for index := range xinput {
				lastIndex := len(xinput) - 1 - index
				last := xinput[lastIndex]
				if itemIndex >= lastIndex {
					break
				}
				if last.size == 0 {
					continue
				}
				if last.size > spaceLeft {
					continue
				}

				for i := range last.size {
					position := item.position + item.origSize + item.filled + i
					id := last.id
					add := position * id

					total = total + add
				}
				item.filled = item.filled + xinput[lastIndex].size
				xinput[lastIndex].size = 0
				spaceLeft = item.free - item.filled
				if spaceLeft == 0 {
					break
				}
			}
		}
		xinput[itemIndex] = item
	}
	for _, item := range xinput {
		for i := range item.size {
			position := item.position + i
			id := item.id
			add := position * id
			total = total + add
		}
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
	l := len(dat)
	print(l)
	check(err)
	return string(dat)
}
