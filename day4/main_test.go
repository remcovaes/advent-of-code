package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestTotalA(t *testing.T) {
	input := `MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX`

	result := TotalResultA(input)
	assert.Equal(t, 18, result)
}

func TestTotalB(t *testing.T) {
	input := `.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........`

	result := TotalResultB(input)
	assert.Equal(t, 9, result)
}

func TestHelper1(t *testing.T) {
	input := `MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX`
	result := GetLeftToRight(input)
	assert.Equal(t, 3, result)
}

func TestHelperRightToLeft(t *testing.T) {
	input := `MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX`
	result := GetRightToLeft(input)
	assert.Equal(t, 2, result)
}

func TestTopToBottom(t *testing.T) {
	input := `MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX`
	result := GetVertical(input)
	assert.Equal(t, 3, result)
}

func TestTopToBottom2(t *testing.T) {
	input := `MSMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
XAXAMASAAA
MAMMMXMMMM
AXMXAXMASX`
	result := GetVertical(input)
	assert.Equal(t, 3, result)
}

func TestHelper4(t *testing.T) {
	input := `MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX`
	result := GetDiagonal(input)
	assert.Equal(t, 4, result)
}

func TestHelper5(t *testing.T) {
	input :=
		`AXAAA
AAMAA
AAAAA
AAAAS`
	result := GetDiagonal(input)
	assert.Equal(t, 1, result)
}
func TestHelper6(t *testing.T) {
	input :=
		`ASAAA
AAAAA
AAAMA
AAAAX`
	result := GetDiagonal(input)
	assert.Equal(t, 1, result)
}
func TestHelper7(t *testing.T) {
	input :=
		`AAASA
AAAAA
AMAAA
XAAAA`
	result := GetDiagonal(input)
	assert.Equal(t, 1, result)
}
func TestHelper8(t *testing.T) {
	input :=
		`AAAAA
AAAAX
AAAMA
AAAAA
ASAAA`
	result := GetDiagonal(input)
	assert.Equal(t, 1, result)
}
func TestHelper9(t *testing.T) {
	input :=
		`AAAAA
XAAAA
AMAAA
AAAAA
AAASA`
	result := GetDiagonal(input)
	assert.Equal(t, 1, result)
}
