package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestTotalA(t *testing.T) {
	input := `7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9`

	result := TotalResultA(input)
	assert.Equal(t, 2, result)
}

func TestIsSafe(t *testing.T) {
	input := []int{7, 6, 4, 2, 1}
	result := IsSafe(input)
	assert.Equal(t, true, result)
}

func TestTotalB(t *testing.T) {
	input := `7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9`

	result := TotalResultB(input)
	assert.Equal(t, 4, result)
}

func TestIsSafeB(t *testing.T) {
	input := []int{8, 6, 4, 4, 1}
	result := IsSafeB(input, false)
	assert.Equal(t, true, result)
}

func TestIsSafeB2(t *testing.T) {
	input := []int{8, 6, 100, 4, 1}
	result := IsSafeB(input, false)
	assert.Equal(t, true, result)
}
func TestIsSafeB3(t *testing.T) {
	input := []int{1, 2, 7, 8, 9}
	result := IsSafeB(input, false)
	assert.Equal(t, false, result)
}
