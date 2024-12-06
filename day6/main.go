package main

import (
	"os"
	"strings"
)

type coordinate struct {
	x int
	y int
}

func TotalResultA(str string) int {
	linesRaw := splitIntoNewlines(str)
	lines := make([][]string, 0)
	for _, line := range linesRaw {
		lines = append(lines, strings.Split(line, ""))
	}

	start, direction := FindStart(lines)
	visited := make(map[coordinate]bool)
	current := start
	currentDirection := direction
	for {
		visited[current] = true
		newPos, newDir, done := GetNextPos(lines, current, currentDirection)
		if done {
			return len(visited)
		}
		current = newPos
		currentDirection = newDir
	}
}

func TotalResultB(str string) int {
	linesRaw := splitIntoNewlines(str)
	lines := make([][]string, 0)
	for _, line := range linesRaw {
		lines = append(lines, strings.Split(line, ""))
	}

	start, direction := FindStart(lines)
	visited := make(map[coordinate]bool)
	current := start
	currentDirection := direction
	for {
		visited[current] = true
		newPos, newDir, done := GetNextPos(lines, current, currentDirection)
		if done {
			break
		}
		current = newPos
		currentDirection = newDir
	}
	current = start
	total := 0
	for coord := range visited {
		hasLoop := HasLoop(lines, coord, start, direction)
		if hasLoop {
			total++
		}
	}

	return total
}

func FindStart(str [][]string) (coordinate, string) {
	for indexY, xline := range str {
		for indexX, current := range xline {
			if current == "^" {
				return coordinate{indexX, indexY}, "up"
			}
			if current == ">" {
				return coordinate{indexX, indexY}, "right"
			}
			if current == "<" {
				return coordinate{indexX, indexY}, "left"
			}
			if current == "v" {
				return coordinate{indexX, indexY}, "down"
			}
		}
	}
	panic("no guard found")
}

func GetNextPos(lines [][]string, current coordinate, direction string) (coordinate, string, bool) {
	if direction == "up" {
		current.y--
	}
	if direction == "down" {
		current.y++
	}
	if current.y < 0 || current.y >= len(lines) {
		return current, "done", true
	}
	if direction == "right" {
		current.x++
	}
	if direction == "left" {
		current.x--
	}

	if current.x < 0 || current.x >= len(lines[0]) {
		return current, "done", true
	}

	if current.y < 0 || current.y >= len(lines[0]) {
		return current, "done", true
	}
	if lines[current.y][current.x] == "#" {
		if direction == "up" {
			current.y++
			x := coordinate{current.x, current.y}
			return x, "right", false
		}
		if direction == "down" {
			current.y--
			return coordinate{current.x, current.y}, "left", false
		}
		if direction == "right" {
			current.x--
			return coordinate{current.x, current.y}, "down", false
		}
		if direction == "left" {
			current.x++
			return coordinate{current.x, current.y}, "up", false
		}
	}
	return coordinate{current.x, current.y}, direction, false
}

func HasLoop(lines [][]string, coordToCheck coordinate, start coordinate, direction string) bool {
	current := start
	currentDirection := direction
	lines[coordToCheck.y][coordToCheck.x] = "#"
	for i := 0; true; i++ {
		if i > 10000 {
			lines[coordToCheck.y][coordToCheck.x] = "."
			return true
		}
		newPos, newDir, done := GetNextPos(lines, current, currentDirection)
		current = newPos
		currentDirection = newDir
		if done {
			break
		}
	}
	lines[coordToCheck.y][coordToCheck.x] = "."

	return false
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
