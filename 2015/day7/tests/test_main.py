import pytest

from advent.main import FullInput, Operation, SingleInput, handle_num_ops, parse_line, read_input, solve_part_one, solve_part_two, solve_part_two_single

def test_noop():
    single_input = SingleInput(
        a=1337,
        b=None,
        operation=Operation.NOOP,
        result="ab"
    )
    full_input = FullInput(
        single=[single_input]
    )
    result = handle_num_ops(full_input, "ab")
    assert result == 1337

def test_and():
    single_input = SingleInput(
        a=3,
        b=1,
        operation=Operation.AND,
        result="ab"
    )
    full_input = FullInput(
        single={}
    )
    full_input.single[single_input.result] = single_input
    result = handle_num_ops(full_input, "ab")
    assert result == 1

def test_and_and_noop():
    noop_input_1 = SingleInput(
        a=1,
        b=None,
        operation=Operation.NOOP,
        result="ab"
    )
    noop_input_2 = SingleInput(
        a=3,
        b=None,
        operation=Operation.NOOP,
        result="bc"
    )
    and_input = SingleInput(
        a="ab",
        b="bc",
        operation=Operation.AND,
        result="abc"
    )
    full_input = FullInput(
        single={}
    )
    full_input.single[noop_input_1.result] = noop_input_1
    full_input.single[noop_input_2.result] = noop_input_2
    full_input.single[and_input.result] = and_input
    result = handle_num_ops(full_input, "abc")
    assert result == 1

def test_part1_total():
    assert solve_part_one(read_input()) == 3176

@pytest.mark.parametrize(
    [ "input_string", "expected" ],
    [
        [ "abc", 3 ],
    ]
)
def test_part2(input_string, expected):
    present = parse_line(input_string)
    assert solve_part_two_single(present) == expected

def test_part2_total():
    assert solve_part_two(read_input()) == 14710
