import functions

N = 100

def print_tests_header(title):
    print("*" * 30)
    print("*", end="")
    print("{:^28s}".format(title), end="")
    print("*")
    print("*" * 30)

def part1(PATH):
    print_tests_header("Part 1")

def part2(PATH):
    print_tests_header("Part 2")
    functions.make_test("ft_substr", PATH, "free(ft_substr(<string>, <uint>, <uint>));", N)

def partB(PATH):
    print_tests_header("Part Bonus")
