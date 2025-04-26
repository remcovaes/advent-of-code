import pytest

from advent.main import solve_part_one, solve_part_two


@pytest.mark.parametrize(
    [ "input_string", "expected" ],
    [
        [ "abcdef", 609043 ],
        [ "yzbqklnj", 282749 ],
    ]
)
def test_part_one_single(input_string, expected):
    assert solve_part_one(input_string) == expected

@pytest.mark.parametrize(
    [ "input_string", "expected" ],
    [
        [ "yzbqklnj", 9962624 ],
    ]
)
def test_part2(input_string, expected):
    assert solve_part_two(input_string) == expected
