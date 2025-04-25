package main

import (
	"math"
	"os"
	"slices"
	"strconv"
	"strings"
)

type data struct {
	leftList  []int
	rightList []int
}

func ParseInput(str string) data {
	splitted := splitIntoNewlines(str)
	leftList := make([]int, 0)
	rightList := make([]int, 0)
	for _, item := range splitted {
		if len(item) == 0 {
			continue
		}
		parts := strings.Split(item, "   ")
		x, _ := strconv.Atoi(parts[0])
		leftList = append(leftList, x)
		x2, _ := strconv.Atoi(parts[1])
		rightList = append(rightList, x2)
	}

	return data{
		leftList:  leftList,
		rightList: rightList,
	}
}

func GetResultsPart1(str string) int {
	parsedData := ParseInput(str)

	leftList := slices.Sorted(parsedData.leftList)
	rightList := parsedData.rightList

	slices.Sort(leftList)
	slices.Sort(rightList)

	total := 0
	for index := range leftList {
		left := leftList[index]
		right := rightList[index]
		total = total + int(math.Abs(float64(left-right)))
	}

	return total
}

func GetResultsPart2(str string) int {
	parsedData := ParseInput(str)

	leftList := parsedData.leftList
	rightList := parsedData.rightList

	slices.Sort(leftList)
	slices.Sort(rightList)
	total := 0
	for _, item := range leftList {
		rightCount := Counts(rightList, item)
		total = total + item*rightCount
	}

	return total
}

func GetTotalPart1() int {
	str := getDataDay()
	return GetResultsPart1(str)
}

func GetTotalPart2() int {
	str := getDataDay()
	return GetResultsPart2(str)
}

func Counts[S []E, E comparable](s S, e E) int {
	var n int
	for _, v := range s {
		if v == e {
			n++
		}
	}
	return n
}

func splitIntoNewlines(str string) []string {
	return strings.Split(str, "\n")
}
func main() {
	println("Result part 1: ", GetTotalPart1())
	println("Result part 2: ", GetTotalPart2())
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
