package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestResultsPartA(t *testing.T) {
	input := `
3   4
4   3
2   5
1   3
3   9
3   3
`

	result := GetResultsPart1(input)
	assert.Equal(t, 11, result)
}

func TestResultsPartB(t *testing.T) {
	input := `3   4
4   3
2   5
1   3
3   9
3   3`

	result := GetResultsPart2(input)
	assert.Equal(t, 31, result)
}

func TestTotalPart1(t *testing.T) {
	assert.Equal(t, 1189304, GetTotalPart1())
}

func TestTotalPart2(t *testing.T) {
	assert.Equal(t, 24349736, GetTotalPart2())
}
