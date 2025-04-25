package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestTotalA(t *testing.T) {
	input := `xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))`

	result := TotalResultA(input)
	assert.Equal(t, 161, result)
}

func TestTotalB(t *testing.T) {
	input := `xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))`

	result := TotalResultB(input)
	assert.Equal(t, 48, result)
}

func TestTotalB2(t *testing.T) {
	input := `xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+m
	ul(32,64](mul(11,8)undo()?mul(8,5))xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))`

	result := TotalResultB(input)
	assert.Equal(t, 48*2, result)
}

func TestHelper1(t *testing.T) {
	input := []int{7, 6, 4, 2, 1}
	result := Helper1(input)
	assert.Equal(t, true, result)
}

func TestHelper2(t *testing.T) {
	input := []int{8, 6, 4, 4, 1}
	result := Helper2(input)
	assert.Equal(t, true, result)
}

func TestHelper3(t *testing.T) {
	input := []int{8, 6, 100, 4, 1}
	result := Helper3(input)
	assert.Equal(t, true, result)
}
