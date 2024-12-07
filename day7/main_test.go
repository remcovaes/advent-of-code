package main

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestTotalA(t *testing.T) {
	input := `190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20`
	result := TotalResultA(input)
	assert.Equal(t, 3749, result)
}

func TestTotalB(t *testing.T) {
	input := ``

	result := TotalResultB(input)
	assert.Equal(t, 0, result)
}

func TestHelper1(t *testing.T) {
	input := Line{190, []int{10, 19}}
	result := IsMul(input)
	assert.Equal(t, true, result)
}

func TestHelper2(t *testing.T) {
	input := Line{3267, []int{81, 40, 27}}
	result := IsMul(input)
	assert.Equal(t, true, result)
}

func TestHelper3(t *testing.T) {
	result := OperationsForLen(2)
	assert.Equal(t, len(result), 4)
}
func TestHelper4(t *testing.T) {
	result := OperationsForLen(3)
	assert.Equal(t, len(result), 8)
}
func TestHelper5(t *testing.T) {
	result := OperationsForLen(4)
	assert.Equal(t, len(result), 16)
}

func TestWithInput(t *testing.T) {
	input := GetDataDay()

	result := TotalResultA(input)
	assert.Equal(t, 1298103531759, result)
}
func TestWithInput2(t *testing.T) {
	input := GetDataDay()

	result := TotalResultB(input)
	assert.Equal(t, 1298103531759, result)
}
func TestWithInput3(t *testing.T) {
	input := `190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20`

	result := TotalResultB(input)
	assert.Equal(t, 11387, result)
}
func TestWithInput7(t *testing.T) {
	input := `7290: 6 8 6 15`

	result := TotalResultB(input)
	assert.Equal(t, 7290, result)
}
func TestCase1(t *testing.T) {
	string := "654381: 11 6 16 20 40 5 7 8 4 9 8"
	line := ParseLine(string)
	assert.Equal(t, true, IsMul(line))
}

func Test5(t *testing.T) {
	line := OperationsForLen(4)
	for _, i := range line {
		fmt.Printf("%v\n", i)
	}
	assert.Equal(t, true, line)
}
