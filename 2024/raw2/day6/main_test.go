package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestExmpleInputPart1(t *testing.T) {
	input := `....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...`
	result := TotalResultA(input)
	assert.Equal(t, 41, result)
}

func TestExmpleInputPart2(t *testing.T) {
	input := `....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...`

	result := TotalResultB(input)
	assert.Equal(t, 6, result)
}

func TestDayInputPart1(t *testing.T) {
	input := GetDataDay()
	result := TotalResultA(input)
	assert.Equal(t, 5534, result)
}

func TestDayInputPart2(t *testing.T) {
	input := GetDataDay()
	result := TotalResultB(input)
	assert.Equal(t, 2262, result)
}
