package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

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

func TestHelper1(t *testing.T) {
	input := ``

	result := Helper1(input)
	assert.Equal(t, 0, result)
}

func TestHelper2(t *testing.T) {
	input := ``

	result := Helper1(input)
	assert.Equal(t, 0, result)
}

func TestHelper3(t *testing.T) {
	input := ``

	result := Helper1(input)
	assert.Equal(t, 0, result)
}
