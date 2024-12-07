package main

import (
	"os"
	"slices"
	"strconv"
	"strings"
)

type Line struct {
	total int
	nums  []int
}

func TotalResultA(str string) int {
	lines := splitIntoNewlines(str)
	parsedLines := make([]Line, 0)
	for _, l := range lines {
		if l == "" {
			continue
		}

		parsedLines = append(parsedLines, ParseLine(l))
	}

	return HandleLines(parsedLines)
}

func TotalResultB(str string) int {
	lines := splitIntoNewlines(str)
	parsedLines := make([]Line, 0)
	for _, l := range lines {
		if l == "" {
			continue
		}

		parsedLines = append(parsedLines, ParseLine(l))
	}

	return HandleLinesB(parsedLines)
}

func ParseLine(str string) Line {
	splitted := strings.Split(str, ":")
	parsedTotal, err := strconv.Atoi(splitted[0])
	if err != nil {
		print(err)
	}
	trimmed := strings.Trim(splitted[1], " ")
	numsStrings := strings.Split(trimmed, " ")
	nums := make([]int, 0)
	for _, numString := range numsStrings {
		parsedNum, _ := strconv.Atoi(numString)
		nums = append(nums, parsedNum)
		if err != nil {
		}
	}

	return Line{parsedTotal, nums}
}

func HandleLines(lines []Line) int {
	total := 0
	for _, line := range lines {
		if IsMul(line) {
			total += line.total
		}
	}
	return total
}

func HandleLinesB(lines []Line) int {
	total := 0
	for _, line := range lines {
		if IsMulB(line) {
			total += line.total
		}
	}
	return total
}
func OperationsForLenB(num int) [][]string {
	total := make([][]string, 0)

	if num == 1 {
		total = append(total, []string{"+"})
		total = append(total, []string{"*"})
		total = append(total, []string{"|"})
		return total
	}

	previous := OperationsForLenB(num - 1)
	for _, item := range previous {
		newArr := make([]string, len(item))
		copy(newArr, item)
		newItem := append(newArr, "+")
		total = append(total, newItem)
	}
	for _, item := range previous {
		newArr := make([]string, len(item))
		copy(newArr, item)
		newItem2 := append(newArr, "*")
		total = append(total, newItem2)
	}
	for _, item := range previous {
		newArr := make([]string, len(item))
		copy(newArr, item)
		newItem2 := append(newArr, "|")
		total = append(total, newItem2)
	}
	slices.SortFunc(total, func(a []string, b []string) int {
		if strings.Join(a, "") > strings.Join(b, "") {
			return 1
		}

		return -1
	})
	return total
}
func OperationsForLen(num int) [][]string {
	total := make([][]string, 0)

	if num == 1 {
		total = append(total, []string{"+"})
		total = append(total, []string{"*"})
		return total
	}

	previous := OperationsForLen(num - 1)
	for _, item := range previous {
		newArr := make([]string, len(item))
		copy(newArr, item)
		newItem := append(newArr, "+")
		total = append(total, newItem)
	}
	for _, item := range previous {
		newArr := make([]string, len(item))
		copy(newArr, item)
		newItem2 := append(newArr, "*")
		total = append(total, newItem2)
	}
	slices.SortFunc(total, func(a []string, b []string) int {
		if strings.Join(a, "") > strings.Join(b, "") {
			return 1
		}

		return -1
	})
	return total
}
func IsMulB(nums Line) bool {
	operators := OperationsForLenB(len(nums.nums) - 1)
	for _, operatorList := range operators {
		total := nums.nums[0]
		for i, operator := range operatorList {
			num2 := nums.nums[i+1]
			if operator == "*" {
				total = total * num2
			}
			if operator == "+" {
				total = total + num2
			}
			if operator == "|" {
				r, _ := strconv.Atoi(strconv.Itoa(total) + strconv.Itoa(num2))
				total = r
			}
		}
		if total > nums.total {
			continue
		}
		if total == nums.total {
			return true
		}
	}
	return false
}
func IsMul(nums Line) bool {
	operators := OperationsForLen(len(nums.nums) - 1)
	for _, operatorList := range operators {
		total := nums.nums[0]
		for i, operator := range operatorList {
			num2 := nums.nums[i+1]
			if operator == "*" {
				total = total * num2
			}
			if operator == "+" {
				total = total + num2
			}
		}
		if total == nums.total {
			return true
		}
	}
	return false
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
