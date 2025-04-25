import pytest

from advent.main import read_input, solve_part_one, solve_part_two


@pytest.mark.parametrize(
    [ "input_string", "expected" ],
    [
        [ "()()", 0 ],
        [ "))(((((", 3],
        [ read_input(), 280 ]
    ]
)
def test_part1(input_string, expected):
    assert solve_part_one(input_string) == expected

@pytest.mark.parametrize(
    [ "input_string", "expected" ],
    [
        [ ")", 1 ],
        [ "()())", 5],
        [ read_input(), 1797 ]
    ]
)
def test_part2(input_string, expected):
    assert solve_part_two(input_string) == expected
