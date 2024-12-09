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
	total := 0

	lines := input.lines
	for index := range len(lines) {

		reversedIndex := len(input.lines) - 1
		nextIndex := 0
		for {
			if nextIndex > reversedIndex {
				break
			}
			next := input.lines[nextIndex]
			last := input.lines[reversedIndex]
			if last.size == 0 {
				reversedIndex--
				continue
			}

			if nextIndex >= reversedIndex {
				input.lines[reversedIndex].filleable = false
				reversedIndex--
				continue
			}
			if input.lines[reversedIndex].size == 0 || !last.filleable {
				reversedIndex--
				continue
			}
			if next.position > last.position {
				break
			}
			if input.lines[reversedIndex].size > next.free {
				nextIndex++
				continue
			}

			for i := range input.lines[reversedIndex].size {
				id := input.lines[reversedIndex].id
				pos := i + next.position + next.size + next.filled
				total += id * pos
			}

			input.lines[nextIndex].free = next.free - last.size
			input.lines[nextIndex].filled += last.size

			input.lines[reversedIndex].size = 0
		}
		if input.lines[index].free < 0 {
			panic("can not happen")
		}
		if input.lines[index].size < 0 {
			panic("can not happen")
		}
	}

	for index := range len(lines) {
		currentLine := input.lines[index]
		for i := range currentLine.size {
			xid := input.lines[index].id
			post := input.lines[index].position + i
			total += xid * post
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
