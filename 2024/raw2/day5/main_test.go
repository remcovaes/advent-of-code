package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestTotalA(t *testing.T) {
	input := `47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
`
	result := TotalResultA(input)
	assert.Equal(t, 143, result)
}

func TestTotalB(t *testing.T) {
	input := `47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
`

	result := TotalResultB(input)
	assert.Equal(t, 123, result)
}

func TestHelper1(t *testing.T) {
	input := `47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13`
	result := ParseRules(input)
	assert.Equal(t, result[13][0], 97)
	assert.Equal(t, len(result[13]), 6)
}

func TestHelper2(t *testing.T) {
	input := []int{75, 47, 61, 53, 29}
	inputRules := `47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13`
	rules := ParseRules(inputRules)
	result := Helper2(rules, input)
	assert.Equal(t, 61, result)
}

func TestHelper3(t *testing.T) {
	input := []int{75, 97, 47, 61, 53}
	inputRules := `47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13`
	rules := ParseRules(inputRules)
	result := Helper3(rules, input)
	assert.Equal(t, 47, result)
}

func TestNewArray(t *testing.T) {
	input := []int{75, 97, 47, 61, 53}
	inputRules := `47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13`
	rules := ParseRules(inputRules)
	result := CorrectArray(rules, input)
	assert.Equal(t, 5, len(result))
	assert.Equal(t, 97, result[0])
	assert.Equal(t, 75, result[1])
	assert.Equal(t, 47, result[2])
	assert.Equal(t, 61, result[3])
	assert.Equal(t, 53, result[4])
}

func TestNewArray2(t *testing.T) {
	input := []int{61, 13, 29}
	inputRules := `47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13`
	rules := ParseRules(inputRules)
	result := CorrectArray(rules, input)
	assert.Equal(t, 3, len(result))
	assert.Equal(t, 61, result[0])
	assert.Equal(t, 29, result[1])
	assert.Equal(t, 13, result[2])
}
