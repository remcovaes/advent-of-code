package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestInput(t *testing.T) {
	input := ``
	result := parseInput(input)

	assert.Equal(t, 0, result)
}

func TestExampleA(t *testing.T) {
	input := ``
	result := TotalResultA(input)
	assert.Equal(t, 0, result)
}

func TestExampleB(t *testing.T) {
	input := ``

	result := TotalResultB(input)
	assert.Equal(t, 0, result)
}

func TestFullA(t *testing.T) {
	input := GetDataDay()
	result := TotalResultA(input)
	assert.Equal(t, 0, result)
}

func TestFullB(t *testing.T) {
	input := GetDataDay()
	result := TotalResultB(input)
	assert.Equal(t, 0, result)
}

func TestHelperPart1(t *testing.T) {
	input := PuzzleInput{}

	result := HelperPart1(input)
	assert.Equal(t, 0, result)
}

func TestHelperSingelPart1(t *testing.T) {
	input := SingleInput{}

	result := HelperSinglePart1(input)
	assert.Equal(t, 0, result)
}

func TestHelperPart2(t *testing.T) {
	input := PuzzleInput{}

	result := HelperPart1(input)
	assert.Equal(t, 0, result)
}

func TestHelperSingelPart2(t *testing.T) {
	input := SingleInput{}

	result := HelperSinglePart2(input)
	assert.Equal(t, 0, result)
}
