package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestTotalA(t *testing.T) {
	input := `
3   4
4   3
2   5
1   3
3   9
3   3
`

	result := TotalResultA(input)
	assert.Equal(t, 11, result)
}
func TestTotal2A(t *testing.T) {
	input := `3   4
4   3
2   5
1   3
3   9
3   3`

	result := TotalResultB(input)
	assert.Equal(t, 31, result)
}
