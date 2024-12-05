package main

import (
	"os"
	"regexp"
	"strings"
)

func TotalResultA(strraw string) int {
	str := strings.Trim(strraw, "\n")
	leftRight := GetLeftToRight(str)
	rightLeft := GetRightToLeft(str)
	topToBot := GetVertical(str)

	diag := GetDiagonal(str)
	return leftRight + rightLeft + topToBot + diag
}

func TotalResultB(strraw string) int {
	str := strings.Trim(strraw, "\n")
	diag := Part2(str)
	return diag
}

func GetLeftToRight(input string) int {
	pattern := regexp.MustCompile("XMAS")
	matches := pattern.FindAllString(input, -1)
	return len(matches)
}

func GetRightToLeft(input string) int {
	pattern := regexp.MustCompile("SAMX")
	matches := pattern.FindAllString(input, -1)
	return len(matches)
}

func GetVertical(input string) int {
	var sb strings.Builder
	splitted := splitIntoNewlines(input)
	for index := 0; index < len(splitted[0]); index++ {
		for _, str := range splitted {
			if len(str) == 0 {
				continue
			}
			sb.WriteByte(str[index])
		}
		sb.WriteString("\n")
	}
	transposed := sb.String()
	left := GetLeftToRight(transposed)
	right := GetRightToLeft(transposed)
	return left + right
}

func GetDiagonalTopLeft(input string) int {
	splitted := splitIntoNewlines(input)
	total := 0
	xlen := len(splitted[0])
	ylen := len(splitted)
	for y := range splitted {
		for x := range splitted[0] {
			check := string(splitted[y][x])
			if check != "X" {
				continue
			}
			if y >= 3 && x >= 3 {
				letter1 := string(splitted[y-3][x-3])
				letter2 := string(splitted[y-2][x-2])
				letter3 := string(splitted[y-1][x-1])
				word := letter3 + letter2 + letter1
				if word == "MAS" {
					total++
				}
			}
			if (xlen-y-1) >= 3 && (ylen-x-1) >= 3 {
				letter1 := string(splitted[y+3][x+3])
				letter2 := string(splitted[y+2][x+2])
				letter3 := string(splitted[y+1][x+1])
				word := letter3 + letter2 + letter1
				if word == "MAS" {
					total++
				}
			}
			if (xlen-y-1) >= 3 && x >= 3 {
				letter1 := string(splitted[y+3][x-3])
				letter2 := string(splitted[y+2][x-2])
				letter3 := string(splitted[y+1][x-1])
				word := letter3 + letter2 + letter1
				if word == "MAS" {
					total++
				}
			}
			if y >= 3 && (ylen-x-1) >= 3 {
				letter1 := string(splitted[y-3][x+3])
				letter2 := string(splitted[y-2][x+2])
				letter3 := string(splitted[y-1][x+1])
				word := letter3 + letter2 + letter1
				if word == "MAS" {
					total++
				}
			}
		}
	}
	return total
}
func Part2(input string) int {
	splitted := splitIntoNewlines(input)
	total := 0
	xlen := len(splitted[0])
	ylen := len(splitted)
	for y := range splitted[0] {
		for x := range splitted {
			if string(splitted[x][y]) != "A" {
				continue
			}
			if x >= 1 && y >= 1 && (xlen-x-1) >= 1 && (ylen-y-1) >= 1 {
				topLeft := string(splitted[x-1][y-1])
				topRight := string(splitted[x-1][y+1])
				bottomLeft := string(splitted[x+1][y-1])
				bottomRight := string(splitted[x+1][y+1])

				letters := topLeft + topRight + bottomLeft + bottomRight
				countM := strings.Count(letters, "M")
				countS := strings.Count(letters, "S")
				if countM != 2 {
					continue
				}
				if countS != 2 {
					continue
				}
				if topLeft == bottomRight {
					continue
				}
				total++
			}
		}
	}
	return total
}
func GetDiagonalTopRight(input string) int {
	var sb strings.Builder
	splitted := splitIntoNewlines(input)
	for _, str := range splitted {
		if len(str) == 0 {
			continue
		}

		sb.WriteString(Reverse(str))
		sb.WriteString("\n")
	}
	transposed := sb.String()
	left := GetDiagonalTopLeft(transposed)
	return left
}

func GetDiagonal(input string) int {
	topLeft := GetDiagonalTopLeft(input)
	return topLeft
}

func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
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
