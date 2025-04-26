import pytest

from advent.main import parse_present, read_input, solve_part_one, solve_part_one_single, solve_part_two, solve_part_two_single


@pytest.mark.parametrize(
    [ "input_string", "expected" ],
    [
        [ "2x3x4", 58 ],
    ]
)
def test_part1(input_string, expected):
    present = parse_present(input_string)
    assert solve_part_one_single(present) == expected

def test_part1_total():
    assert solve_part_one(read_input()) == 1598415

@pytest.mark.parametrize(
    [ "input_string", "expected" ],
    [
        [ "2x3x4", 34 ],
        [ "1x1x10", 14 ],
        [ "3x4x2", 34 ],
    ]
)
def test_part2(input_string, expected):
    present = parse_present(input_string)
    assert solve_part_two_single(present) == expected

def test_part2_total():
    assert solve_part_two(read_input()) != 3828105
    assert solve_part_two(read_input()) == 3812909
