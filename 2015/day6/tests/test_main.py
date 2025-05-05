from advent.main import parse_line, read_input, solve_part_one, solve_part_two

def test_parsing():
    result = parse_line("turn off 150,300 through 213,740")
    assert result.action == "off"
    assert result.start.x == 150
def test_part1_total():
    assert solve_part_one(read_input()) > 377035
    assert solve_part_one(read_input()) == 377891


def test_part2_total():
    assert solve_part_two(read_input()) == 14110788
