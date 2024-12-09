package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestInput(t *testing.T) {
	input := `2333133121414131402`
	result := parseInput(input)

	assert.Equal(t, 0, result.lines[0].position)
	assert.Equal(t, 5, result.lines[1].position)
	assert.Equal(t, 11, result.lines[2].position)
}

func TestExampleA(t *testing.T) {
	input := `2333133121414131402`
	result := TotalResultA(input)
	assert.Equal(t, 1928, result)
}

func TestExampleA2(t *testing.T) {
	input := `2222`
	result := TotalResultA(input)
	assert.Equal(t, 5, result)
}

func TestExampleA3(t *testing.T) {
	input := `0055`
	result := TotalResultA(input)
	assert.Equal(t, 10, result)
}
func TestExampleA4(t *testing.T) {
	input := `233313312141413140211`
	result := TotalResultA(input)
	assert.Equal(t, 2132, result)
}
func TestExampleB(t *testing.T) {
	input := `2333133121414131402`

	result := TotalResultB(input)
	assert.Equal(t, 2858, result)
}

func TestExampleB8(t *testing.T) {
	input := `0255`
	result := TotalResultB(input)
	assert.Equal(t, 20, result)
}

func TestExampleB9(t *testing.T) {
	input := `0402020202021010`
	result := TotalResultB(input)
	assert.Equal(t, 20, result)
}

func TestFullA(t *testing.T) {
	input := GetDataDay()
	result := TotalResultA(input)
	assert.NotEqual(t, 5429477700138, result)
	assert.NotEqual(t, 5740152760912, result)
	assert.NotEqual(t, 5429477700138, result)
	assert.NotEqual(t, 6306903074866, result)
	assert.NotEqual(t, 6307445652781, result)
	assert.NotEqual(t, 5545833186977, result)
	assert.NotEqual(t, 6305450446611, result)

	assert.Equal(t, 0, result)
}

func TestFullB(t *testing.T) {
	input := GetDataDay()
	result := TotalResultB(input)
	assert.Greater(t, 7886024298205, result)
	assert.Greater(t, 7885488892615, result)
	assert.NotEqual(t, 10126771850879, result)
	assert.NotEqual(t, 8439434080946, result)
	assert.NotEqual(t, 6352282411068, result)
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
