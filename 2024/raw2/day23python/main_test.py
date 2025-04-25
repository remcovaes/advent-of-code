from main import solve_total_1, solve_total_2, solver_part1, solver_part2

def test_total_1():
    result = solve_total_1()
    assert result == 0

def test_example_1():
    input = """
wq-aq
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""
    result = solver_part1(input)
    assert result == 1

def test_total_2():
    result = solve_total_2()
    assert result == 0
def test_example_2_small():
    input = """
ab-cd
cd-ef
ef-ab
ef-qw
"""
    result = solver_part2(input)
    assert result == "ab,cd,ef"
def test_example_2_longer():
    input = """
ab-cd
cd-ef
ef-gh
gh-ij
ij-ab
ef-qw
ab-cd
cd-ef
ef-ab
ef-cd
cd-ef
ef-ab
"""
    result = solver_part2(input)
    assert result == "ab,cd,ef,gh,ij"


def test_example_2():
    input = """
ka-co
wq-aq
kh-tc
qp-kh
de-cg
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""
    result = solver_part2(input)
    assert result == "co,de,ka,ta"

