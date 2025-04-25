package main

import (
	"os"
	"strings"
)

type Coor struct {
	x int
	y int
}

func TotalResultA(str string) int {
	parsed := SplitIntoStringLines(str)
	pairs := FindLetters(parsed)
	foundTotal := make([]Coor, 0)
	for _, pair := range pairs {
		found := FindNewPos(pair, parsed)
		foundTotal = append(foundTotal, found...)

	}

	deduped := removeDuplicate(foundTotal)
	return len(deduped)
}

func SplitIntoStringLines(str string) [][]string {
	splitted := strings.Split(str, "\n")
	parsed := make([][]string, 0)
	for _, item := range splitted {
		if item == "" {
			continue
		}
		letters := strings.Split(item, "")
		parsed = append(parsed, letters)
	}
	return parsed
}

func TotalResultB(str string) int {
	parsed := SplitIntoStringLines(str)
	pairs := FindLetters(parsed)
	foundTotal := make([]Coor, 0)
	for _, pair := range pairs {
		found := FindNewPosB(pair, parsed)
		foundTotal = append(foundTotal, found...)

	}

	deduped := removeDuplicate(foundTotal)

	return len(deduped)
}

func FindLetters(str [][]string) map[string][]Coor {
	result := make(map[string][]Coor, 0)
	for y, row := range str {
		for x, char := range row {
			if char == "." {
				continue
			}
			arr, exists := result[char]
			newPos := Coor{y: y, x: x}
			if !exists {
				result[char] = []Coor{newPos}
				continue
			}
			result[char] = append(arr, newPos)
		}
	}
	return result
}

func GetNewCoords(first Coor, second Coor) []Coor {
	newCoors := make([]Coor, 0)
	Coor1 := Coor{x: first.x - (first.x - second.x), y: first.y - (first.y - second.y)}
	if Coor1 != first && Coor1 != second {
		newCoors = append(newCoors, Coor1)
	}
	Coor2 := Coor{x: first.x + (first.x - second.x), y: first.y + (first.y - second.y)}
	if Coor2 != first && Coor2 != second {
		newCoors = append(newCoors, Coor2)
	}
	Coor3 := Coor{x: second.x - (first.x - second.x), y: second.y - (first.y - second.y)}
	if Coor3 != first && Coor3 != second {
		newCoors = append(newCoors, Coor3)
	}
	Coor4 := Coor{x: second.x + (first.x - second.x), y: second.y + (first.y - second.y)}
	if Coor4 != first && Coor4 != second {
		newCoors = append(newCoors, Coor4)
	}
	return newCoors
}

func GetNewCoordsB(first Coor, second Coor, edge int) []Coor {
	newCoors := make([]Coor, 0)
	newCoors = append(newCoors, first)
	newCoors = append(newCoors, second)
	for i := 1; i < 50; i++ {
		diffx := (first.x - second.x) * i
		diffy := (first.y - second.y) * i

		c := Coor{x: first.x - diffx, y: first.y - diffy}
		if c.x < 0 || c.y < 0 || c.x >= edge || c.y >= edge {
			break
		}
		if c != first && c != second {
			newCoors = append(newCoors, c)
		} else {
			break
		}
	}
	for i := 1; i < 50; i++ {
		diffx := (first.x - second.x) * i
		diffy := (first.y - second.y) * i
		c := Coor{x: first.x + diffx, y: first.y + diffy}
		if c.x < 0 || c.y < 0 || c.x >= edge || c.y >= edge {
			break
		}
		if c != first && c != second {
			newCoors = append(newCoors, c)
		} else {

			break
		}

	}
	for i := 1; i < 50; i++ {
		diffx := (first.x - second.x) * i
		diffy := (first.y - second.y) * i
		c := Coor{x: second.x - diffx, y: second.y - diffy}
		if c.x < 0 || c.y < 0 || c.x >= edge || c.y >= edge {
			break
		}
		if c != first && c != second {
			newCoors = append(newCoors, c)
		} else {

			break
		}

	}
	for i := 1; i < 50; i++ {
		diffx := (first.x - second.x) * i
		diffy := (first.y - second.y) * i
		c := Coor{x: second.x + diffx, y: second.y + diffy}
		if c.x < 0 || c.y < 0 || c.x >= edge || c.y >= edge {
			break
		}
		if c != first && c != second {
			newCoors = append(newCoors, c)
		} else {

			break
		}

	}
	return newCoors
}
func FindNewPosB(coords []Coor, input [][]string) []Coor {
	if len(coords) == 0 {
		return make([]Coor, 0)
	}
	newCoords := make([]Coor, 0)
	for _, firstCoor := range coords {
		secondCoor := coords[0]
		current := GetNewCoordsB(firstCoor, secondCoor, len(input))
		for _, newCurrent := range current {
			if newCurrent.y >= 0 && newCurrent.y < len(input) && newCurrent.x >= 0 && newCurrent.x < len(input[0]) {
				newCoords = append(newCoords, newCurrent)
			}
		}
	}
	next := FindNewPosB(coords[1:], input)
	for _, item := range next {
		newCoords = append(newCoords, item)
	}
	return newCoords
}
func FindNewPos(coords []Coor, input [][]string) []Coor {
	if len(coords) == 0 {
		return make([]Coor, 0)
	}
	newCoords := make([]Coor, 0)
	for _, firstCoor := range coords {
		secondCoor := coords[0]
		current := GetNewCoords(firstCoor, secondCoor)
		for _, newCurrent := range current {
			if newCurrent.y >= 0 && newCurrent.y < len(input) && newCurrent.x >= 0 && newCurrent.x < len(input[0]) {
				newCoords = append(newCoords, newCurrent)
			}
		}
	}
	next := FindNewPos(coords[1:], input)
	for _, item := range next {
		newCoords = append(newCoords, item)
	}
	return newCoords
}

func Helper3(str string) int {
	return 0
}

func splitIntoNewlines(str string) []string {
	return strings.Split(str, "\n")
}

func removeDuplicate[T comparable](sliceList []T) []T {
	allKeys := make(map[T]bool)
	list := []T{}
	for _, item := range sliceList {
		if _, value := allKeys[item]; !value {
			allKeys[item] = true
			list = append(list, item)
		}
	}
	return list
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
