package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestTotalA(t *testing.T) {
	input := ``
	result := TotalResultA(input)
	assert.Equal(t, 143, result)
}

func TestTotalB(t *testing.T) {
	input := ``

	result := TotalResultB(input)
	assert.Equal(t, 123, result)
}

func TestHelper1(t *testing.T) {
	input := ``
	result := Helper1(input)
	assert.Equal(t, result, 6)
}

func TestHelper2(t *testing.T) {
	input := ``
	result := Helper2(input)
	assert.Equal(t, result, 6)
}

func TestHelper3(t *testing.T) {
	input := ``
	result := Helper3(input)
	assert.Equal(t, result, 6)
}
